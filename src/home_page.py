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
from bottle import route, run, debug, template, request

# DB Connection
con = sqlite3.connect('./db/sample.db')
# Table Name
sWUser = 'userdb1' #dw_user
sWDryDay = 'dryday' #dw_dryday

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

def fValidateUser(lUserValues):
	"""
	Validate if the Email user entered already exists in db.
	
	If True user re-directed to the signup with error stating
	user email you entered already exists. Try Again.
	If False, user allowed to sign up
	"""
	gDBConn = con.cursor()
	gDBConn.execute("select email from "+sWUser+" where email = '"+lUserValues[2]+"'")
	vUserExist = gDBConn.fetchall()
	print vUserExist
	return vUserExist


def fNewUserData(lHtmlFields, sWUser):
	"""
	Parse user inputs and put save it in db. retrun user entered fields.
	
	Extract user entered fields from lHtmlFields. Call validate function
	before saving it to the db. Table schema for the user table is - 
	CREATE TABLE dw_user (first_name char(30), last_name char(30) ,email varchar(50), pri_state char(30) , sec_state char(30), primary key (email, pri_state) )
	
	"""
	lUserValues= []	
	for sEntry in lHtmlFields:
		lUserValues.append(request.GET.get(sEntry).strip())		
	if len(fValidateUser(lUserValues))>0:
		return []
	gDBConn = con.cursor()
	gDBConn.execute("insert into "+sWUser+" ("+lHtmlFields[0]+","+lHtmlFields[1]+","+lHtmlFields[2]+","+lHtmlFields[3]+") \
		values (?,?,?,?)",(lUserValues[0], lUserValues[1], lUserValues[2], lUserValues[3]))
	con.commit()
	gDBConn.close()
	return lUserValues

@route('/new', method='GET')
def new_user():
	if request.GET.get('save','').strip():
		lHtmlFields= ['first_name', 'last_name', 'email', 'state']
		lUserValues = fNewUserData(lHtmlFields, sWUser)
		if (lUserValues == []):
			return template('userexists.tpl')
		else:
			return template('success.tpl')
	else:
		return template('new_user.tpl')

def fAllDryDays():
	"""
	list all dry days of all state.
	Implimentation missing. AJAX implimentation expected
	Table schema for the dryday table
	CREATE TABLE dw_dryday (drydate integer, state char(30) , primary key(drydate,state) )
	
	"""
	gDBConn.execute("select * from "+sWDryDay+"")
	vAllDays = gDBConn.fetchall()
	return dict(vAllDays)

# Push all state and dry days to js in the file.
# js to store it for faster rendering
"""@route('/alldrydays', method='GET')
def list_all_drydays():
	vAllDryDays = fAllDryDays()
	return template('listalldryday.tpl')
"""

# Temporary function. The main email function to store default details which will be used in email functions across.
# fMainEmail -> fSuccessEmail 
# fMainEmail -> fDryDayEmail 
def fMainEmail (lUserValues):
		sender='mail@whenisdryday.in'
		message = """From: Dry Day <tequila@whenisdryday.in>
		To: %s <%s>
		Subject: Tomorrow is dry day
		This is a test e-mail message.
		LETS HAVE A TEQUILA
		"this is the image location %s
		Tomorrow is a dry day in %s
		""" %(lUserValues[0], lUserValues[1], lUserValues[2], lUserValues[3])
		s.sendmail(sender, email, message)
		print "Successfully sent email"

debug(True) #not in production. same for reloader=True

run(host='localhost', port=8080, reloader=True)
