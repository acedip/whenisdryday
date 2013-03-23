#!/usr/bin/python

#	whenisdryday.in is a email subscription based service to inform users 
#	when is a dry day in India.
#	Copyright (C) 2013  Anirudh singh shekhawat shekhawat.anirudh@gmail.com
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, version 3 of the License.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details http://www.gnu.org/licenses

import sqlite3
import datetime
from bottle import route, run, debug, template, request
from email.mime.text import MIMEText

# DB Connection
con = sqlite3.connect('./db/sample.db')
# sqlite3 unicode to string conversion
con.text_factory = str
# Table Name
sWUser = 'dw_user'
sWUserLive = 'dw_user_live'
sWDryDay = 'dw_dryday'

'''
import smtplib
# SES | Mail connection
#s = smtplib.SMTP("email-smtp.us-east-1.amazonaws.com")
s = smtplib.SMTP("ses-smtp-prod-335357831.us-east-1.elb.amazonaws.com")
s.starttls()
from ses_cred import ses_cred as ses
user_name = ses.cred['user']
user_pswd = ses.cred['pswd']
s.login(user_name,user_pswd)
'''

def check_dryday():
	gDBConn = con.cursor()
	gDBConn.execute("SELECT a.first_name, a.last_name, a.email, a.state1, a.state2, a.state3 \
	FROM "+sWUserLive+" AS a \
	INNER JOIN "+sWDryDay+" AS b \
		ON a.state1=b.state \
			OR a.state2=b.state \
			OR a.state3=b.state \
	WHERE  b.drydate=date('now','+1 day')\
	AND a.verified=1"
	)
	tUserData = gDBConn.fetchall()
	gDBConn.close()
	return tuple (tUserData)

def fSuccessMail(dUserInfo):
	"""
	function argument = state of the successful user
	Returns all dry days in that state
	"""
	gDBConn = con.cursor()
	gDBConn.execute("select * from "+sWDryDay+" where state in (?,?,?)",(dUserInfo['state1'],dUserInfo['state2'],dUserInfo['state3']))
	tState = gDBConn.fetchall()	
	#Tomorrow Dry Day
	gDBConn.execute("SELECT * FROM ( \
	SELECT a.state1 FROM "+sWUserLive+" AS a INNER JOIN "+sWDryDay+" AS b ON a.state1=b.state WHERE  email = '"+dUserInfo['email']+"' AND b.drydate=date('now','+1 day') \
	UNION \
	SELECT a.state2 FROM "+sWUserLive+" AS a INNER JOIN "+sWDryDay+" AS b ON a.state2=b.state WHERE  email = '"+dUserInfo['email']+"' AND b.drydate=date('now','+1 day')  \
	UNION \
	SELECT a.state3 FROM "+sWUserLive+" AS a INNER JOIN "+sWDryDay+" AS b ON a.state3=b.state WHERE  email = '"+dUserInfo['email']+"' AND b.drydate=date('now','+1 day') ) ")
	
	result = tuple ( gDBConn.fetchall() )

	gDBConn.close()

	return template ('dryday_mail.tpl', dUserInfo=dUserInfo, tstate=tState,tResult=result)

me = 'tequila@whenisdryday.in'

def fSendMail(me,tUserData):
	"""
	Email Sending
	fSuccessEmail called and fed into the MIME Text as msg
	msg is a list. with values like sender, subject etc
	Returns success if email sent
	"""
	
	lUserFields= ['first_name', 'last_name', 'email', 'state1', 'state2', 'state3']	
	for row in tUserData:
		dUserInfo = dict(zip(lUserFields,row))
		print dUserInfo
		msg = MIMEText(fSuccessMail(dUserInfo))
		msg['Subject'] = 'Subscription to whenisdryday.in successful'
		msg['From'] = me
		msg['To'] = dUserInfo['email']
		you = dUserInfo['email']
		# Commenting sending as it wouldn't work right now
		#gMail.sendmail(me, you, msg.as_string())
		print "message successully sent"
		vMailTS = datetime.datetime.now()
		fMail = './sent_mail_archives/'+dUserInfo['email']+'_TimeStamp_'+str(vMailTS)+'.html'
		f=open(fMail,'w')
		print >> f, msg.as_string()
		f.close()
	return 1

tUserData = check_dryday()

print tUserData

fSendMail(me,tUserData)


