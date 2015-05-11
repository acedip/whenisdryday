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
import time
from bottle import route, run, debug, template, request, static_file
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from multiprocessing.connection import Client
import cPickle as pickle
import errno, socket
import sys

gMailTS = datetime.datetime.now()

# DB Connection
con = sqlite3.connect('./src/db/dryday.db')
#con = sqlite3.connect('./src/db/test.db')
# sqlite3 unicode to string conversion
con.text_factory = str
# Table Name
sWUser = 'dw_user'
sWUserLive = 'dw_user_live'
sWDryDay = 'dw_dryday'

#execute("create table dw_dryday (state text, reason text, drydate text)")
#execute("create table dw_user (name text, email text, state text, phone integer)")
#execute("create table dw_user_live (name text, email text, state text, phone integer)")

def fPostToServer(sMe,sSubject,email_html,dUserInfo,sSMS):
	"""
	sends email and sms to the post office server
	"""
	address = ('localhost',6000)
	connTCP = Client(address, authkey='')
	dEMAIL = {'id':'email', 'from':sMe, 'subject': sSubject, 'body': email_html ,'to':dUserInfo['email'],'state':dUserInfo['state']}
	dSMS = {'id':'sms', 'sms':sSMS, 'phone':dUserInfo['phone'],'state':dUserInfo['state']}	
	connTCP.send(pickle.dumps(dSMS))
	connTCP.close()
	connTCP = Client(address, authkey='')
	connTCP.send(pickle.dumps(dEMAIL))
	connTCP.close()


def fValidateUser(dUserInfo):
	"""
	Validate if the Email and State user entered already exists in db.
	If True, user asked to Try again with different state
	If False, user allowed to sign up
	"""
	gDBConn = con.cursor()
	gDBConn.execute("select state from "+sWUserLive+" where state = '"+dUserInfo['state']+"' and email = '"+dUserInfo['email']+"' ")
	vUserExist = gDBConn.fetchall()
	if len(vUserExist)>0:
		return 0
	else:
		return 1

def fSuccessMail(dUserInfo,sUserNxtDryDayDtl):
	gDBConn = con.cursor()
	gDBConn.execute("select reason, drydate from "+sWDryDay+" where state = '"+dUserInfo['state']+"' and strftime('%Y',drydate)=strftime('%Y','now') order by drydate")
	sUserAllDryDay=tuple(gDBConn.fetchall())
	lStateBanner=('Maharashtra','Delhi','Tamilnadu','West Bengal')
	dStateBanner={'Maharashtra':'http://whenisdryday.in/bs/img/mail/maha1.jpg','Delhi':'http://whenisdryday.in/bs/img/mail/del1.jpg'\
	,'West Bengal':'http://whenisdryday.in/bs/img/mail/wb1.jpg','Tamilnadu':'http://whenisdryday.in/bs/img/mail/tn1.jpg'}
	return template ('./src/mail/signup_success.tpl', dUserInfo=dUserInfo, sUserAllDryDay=sUserAllDryDay, sUserNxtDryDayDtl=sUserNxtDryDayDtl,dStateBanner=dStateBanner,lStateBanner=lStateBanner)

def fSendMail(dUserInfo,sUserNxtDryDay):
	"""
	Email Sending
	fSuccessEmail called and fed into the MIME Text as msg
	msg is a list. with values like sender, subject etc
	Returns success if email sent
	"""
	sUserNxtDryDayDtl = {'id':'homepage', 'msg':'Next DryDay is on ', 'day':time.strftime('%A',sUserNxtDryDay), 'date':time.strftime('%d',sUserNxtDryDay), 'month':time.strftime('%b',sUserNxtDryDay) }
#	email_html = MIMEText(fSuccessMail(dUserInfo,sUserNxtDryDayDtl),'html')
	email_html = (fSuccessMail(dUserInfo,sUserNxtDryDayDtl))
	sSubject = 'Successfully subscribed to whenisdryday.in'
	sMe = 'tequila@whenisdryday.in'
	sSMS = 'Cheers!!You will be notified by SMS before DryDays in '+dUserInfo['state']+'. '+sUserNxtDryDayDtl['msg']+sUserNxtDryDayDtl['day']+' '+sUserNxtDryDayDtl['date']+' '+sUserNxtDryDayDtl['month']+''
	try :
		fPostToServer(sMe,sSubject,email_html,dUserInfo,sSMS)
		#print "message successully sent" AND DELETE THE MAIL ARCHIVE, KEEP ONLY FILE
		fMail1 = './src/mail/'+str(gMailTS)+'_'+dUserInfo['email']+'_'+dUserInfo['state']+'.html'
		f1=open(fMail1,'w')
		print >> f1, email_html
		f1.close()
		print "email and sms successfully posted to post office server"
		flog='./src/log/homepage_to_post_sucess.log'
		sMsg=''+str(gMailTS)+' Name= '+dUserInfo['name']+' State= '+dUserInfo['state']+' Email= '+dUserInfo['email']+' and Phone= '+str(dUserInfo['phone'])+''
		f=open(flog,'a')
		print >> f, sMsg
		f.close()
	except :
		allerror = sys.exc_info()[0]
		print "error in sending to post office server"
		fsockerr = './src/log/homepage_to_post_error.log'
		sferr = ''+str(gMailTS)+' Name= '+dUserInfo['name']+' State= '+dUserInfo['state']+' Email= '+dUserInfo['email']+' and Phone= '+str(dUserInfo['phone'])+''
		f2=open(fsockerr,'a')
		print >>f2, sferr,allerror
		f2.close
	return 1

def fNewUserData(lHtmlFields):
	"""
	Parse user inputs and put save it in db. retrun user entered fields.
	Extract user entered fields from lHtmlFields. Call validate function
	before saving it to the db. 
	"""
	dUserInfo= {}
	for sEntry in lHtmlFields:
		dUserInfo[sEntry]= request.GET.get(sEntry).strip()
	if (fValidateUser(dUserInfo)==0):
		dUserInfo['state']="State Exists"
		return dUserInfo
	gDBConn = con.cursor()

#	Insert into live table
	gDBConn.execute("insert into "+sWUserLive+" values (?,?,?,?)",(dUserInfo['name'], dUserInfo['email'], dUserInfo['state'], dUserInfo['phone']))

	if (fValidateUser(dUserInfo)==1):
#	Insert into mother table
		gDBConn.execute("insert into "+sWUser+" values (?,?,?,?)",(dUserInfo['name'], dUserInfo['email'], dUserInfo['state'], dUserInfo['phone']))

	con.commit()
	#Next Dry day in user's state to put in email and sms
	gDBConn.execute("SELECT b.drydate\
		FROM ( SELECT min(strftime('%s',drydate)) as min_u FROM "+sWDryDay+" \
			WHERE strftime('%s',drydate)>strftime('%s',date('now')) AND state='"+dUserInfo['state']+"') AS a \
		INNER JOIN "+sWDryDay+" AS b \
			ON a.min_u = strftime('%s',b.drydate)\
		GROUP BY 1")
	tUserDryDay=gDBConn.fetchall()
	sUserNxtDryDay=str(''.join(tUserDryDay[0]))
	sUserNxtDryDay=time.strptime(sUserNxtDryDay,'%Y-%m-%d')
	gDBConn.close()
	fSendMail(dUserInfo,sUserNxtDryDay)
	return dUserInfo

@route('/', method='GET')
def new_user():
	if request.GET.get('save','').strip():
		lHtmlFields= ['name', 'email', 'phone', 'state']
		dUserInfo = fNewUserData(lHtmlFields)
		if (dUserInfo['state'] == "State Exists"):
			return template('user_state_exist.tpl')
		else:
			return template('success.tpl',dUserInfo=dUserInfo)
	else:
		return template('index.tpl')

@route('/unsubscribe/:email', method='GET')
def unsubscribe_user(email):
	if request.GET.get('save','').strip():	
		gDBConn = con.cursor()
		gDBConn.execute("DELETE FROM "+sWUserLive+" WHERE email = '"+email+"' ")
		con.commit()
		gDBConn.close()
		return template('unsubscribe_success.tpl')
	if request.GET.get('cancel','').strip():
		return wetdays()
	else:
		return template('unsubscribe.tpl',emailid=email)

@route('/update/:email', method='GET')
def update_user(email):
	if request.GET.get('save','').strip():	
		dUserUpdateInfo= {}
		lHtmlFields= ['state']
		for sEntry in lHtmlFields:
			dUserUpdateInfo[sEntry]= request.GET.get(sEntry).strip()
		gDBConn = con.cursor()
		gDBConn.execute("UPDATE "+sWUserLive+" SET state = %s WHERE email=%s",(dUserUpdateInfo['state'],email ))
		con.commit()
		gDBConn.close()
		return template('update_success.tpl',lState=dUserUpdateInfo['state'])
	else:
		gDBConn = con.cursor()
		gDBConn.execute("SELECT state FROM "+sWUserLive+" WHERE email = %s",(email,))
		dbresult = gDBConn.fetchone()
		gDBConn.close()
		for row in dbresult:
			lState=row
		return template ('update.tpl',lState=lState,email=email)

@route('/about')
def about():
	return template('about.html')

@route('/wetdays')
def wetdays():
	return template('wetdays.html')

@route('/alldrydays')
def alldrydays():
	return template('alldrydays.html')

@route('/bs/:path#.+#',name='bs')
def db(path):
	return static_file(path,root='bs')

#REMOVE THIS LINE TOO 
@route('/src/mail/:path#.+#',name='mail')
def db(path):
	return static_file(path,root='mail')

@route('/confirm/bs/:path#.+#',name='bs')
def db(path):
	return static_file(path,root='bs')

@route('/update/bs/:path#.+#',name='bs')
def db(path):
	return static_file(path,root='bs')

@route('/unsubscribe/bs/:path#.+#',name='bs')
def db(path):
	return static_file(path,root='bs')

#Load testing on https://loader.io/
@route('/loaderio-2f6667560533b77f3099c56159bdb824/')
def loadtest():
	return template('loadtest.tpl')

debug(True)

run(host='0.0.0.0',port=80,reloader=True)
