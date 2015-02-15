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

import MySQLdb as mdb
import datetime
from bottle import route, run, debug, template, request, static_file
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from multiprocessing.connection import Client
import cPickle as pickle

# DB Connection
con = mdb.connect('localhost', 'testuser', 'test1', 'testdb')
# Table Name
sWUser = 'dw_user'
sWUserLive = 'dw_user_live'
sWDryDay = 'dw_dryday'

def fPostMailToServer(sMsg):
	"""
	The email server is listening on port number 6000.
	Post the email to the server.
	Makes the process of sending email non-blocking.
	"""
	address = ('localhost',6000)
	connTCP = Client(address, authkey='drydayiswhen')
	connTCP.send(pickle.dumps(sMsg))  # pickle ensures that the actual datatype of sMsg doesn't change when it is received on the server
	connTCP.close()

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

def fValidateUser(dUserInfo,sWTable):
	"""
	Validate if the Email user entered already exists in db.
	
	If True user re-directed to the signup with error stating
	user email you entered already exists. Try Again.
	If False, user allowed to sign up
	"""
	gDBConn = con.cursor()
	gDBConn.execute("select email from "+sWTable+" where email = '"+dUserInfo['email']+"'")
	vUserExist = gDBConn.fetchall()
	if len(vUserExist)>0:
		return 0
	else:
		return 1

def fSuccessMail(dUserInfo):
	"""
	function argument = state of the successful user
	Returns all dry days in that state
	create table dw_dryday (state varchar(50), drydate date, dryday varchar(30), primary key (state, drydate));
	"""
	gDBConn = con.cursor()
	
	gDBConn.execute("select state, drydate from "+sWDryDay+" where state = %s",(dUserInfo['state']))
	tState = gDBConn.fetchall()		
	return template ('mail/mail.tpl', dUserInfo=dUserInfo, tstate=tState)

me = 'tequila@whenisdryday.in'

def fSendMail(me,dUserInfo):
	"""
	Email Sending
	fSuccessEmail called and fed into the MIME Text as msg
	msg is a list. with values like sender, subject etc
	Returns success if email sent
	"""
	email_html = MIMEText(fSuccessMail(dUserInfo),'html')
	msg = MIMEMultipart('alternative')
	msg['Subject'] = 'Subscription to whenisdryday.in successful'
	msg['From'] = me
	msg['To'] = dUserInfo['email']
	#you = dUserInfo['email']
	msg.attach(email_html)
	# Commenting sending as it wouldn't work right now
	#gMail.sendmail(me, you, msg.as_string())
	print "message successully sent"
	fPostMailToServer(msg) #Post message as MIMEText
	return 1

def fNewUserData(lHtmlFields, sWUser):
	"""
	Parse user inputs and put save it in db. retrun user entered fields.
	Extract user entered fields from lHtmlFields. Call validate function
	before saving it to the db. Table schema for the user table is -
	 
	create table dw_user (first_name char(30), last_name char(30) ,email varchar(50) primary key, state char(30) , verified int);

	create table dw_user_live (first_name char(30), last_name char(30) ,email varchar(50) primary key, state char(30) , verified int);
	
	"""
	dUserInfo= {}
	for sEntry in lHtmlFields:
		dUserInfo[sEntry]= request.GET.get(sEntry).strip()
	if (fValidateUser(dUserInfo,sWUserLive)==0):
		dUserInfo['first_name']="User Exists"
		return dUserInfo
	gDBConn = con.cursor()
	
#	Insert into live table
	gDBConn.execute("insert into "+sWUserLive+" (first_name,last_name,email,state,verified) values (%s,%s,%s,%s,%s)",(dUserInfo['first_name'], dUserInfo['last_name'], dUserInfo['email'], dUserInfo['state'], dUserInfo['verified']))

	if (fValidateUser(dUserInfo,sWUser)==1):
#	Insert into mother table
		gDBConn.execute("insert into "+sWUser+" (first_name,last_name,email,state,verified) values (%s,%s,%s,%s,%s)",(dUserInfo['first_name'], dUserInfo['last_name'], dUserInfo['email'], dUserInfo['state'], dUserInfo['verified']))
		
	con.commit()
	gDBConn.close()
	fSendMail(me,dUserInfo)
	return dUserInfo

@route('/', method='GET')
def new_user():
	if request.GET.get('save','').strip():
		lHtmlFields= ['first_name', 'last_name', 'email', 'state','verified']
		dUserInfo = fNewUserData(lHtmlFields, sWUser)
		if (dUserInfo['first_name'] == "User Exists"):
			return template('user_exist.tpl')
		else:
			return template('success.tpl')
	else:
		return template('index.tpl')

@route('/confirm/:email', method='GET')
def confirm_user(email):
	gDBConn = con.cursor()
	gDBConn.execute("UPDATE "+sWUserLive+" SET verified = ? WHERE email = %s",(1,email))
	con.commit()
	gDBConn.close()
	return template('<b> emailid {{email}} successully verified </b>',email=email)

@route('/unsubscribe/:email', method='GET')
def unsubscribe_user(email):
	if request.GET.get('save','').strip():	
		gDBConn = con.cursor()
		gDBConn.execute("DELETE FROM "+sWUserLive+" WHERE email = %s",(email,))
		con.commit()
		gDBConn.close()
		return template('unsubscribe_success.tpl')
	else:
		return template ('unsubscribe.tpl',emailid=email)

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

@route('/about.html')
def about():
	return template('about.html')

@route('/wetdays.html')
def about():
	return template('wetdays.html')

@route('/bs/:path#.+#',name='bs')
def db(path):
	return static_file(path,root='bs')

@route('/confirm/bs/:path#.+#',name='bs')
def db(path):
	return static_file(path,root='bs')

@route('/update/bs/:path#.+#',name='bs')
def db(path):
	return static_file(path,root='bs')

@route('/unsubscribe/bs/:path#.+#',name='bs')
def db(path):
	return static_file(path,root='bs')

debug(True)

run(host='0.0.0.0',port=80,reloader=True)
