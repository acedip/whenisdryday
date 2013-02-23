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
import smtplib

state_pics = {
'andhra pradesh'	:'./state_pics/andhrapradesh.jpg' ,\
'arunachal pradesh'	:'./state_pics/arunachalpradesh.jpg' ,\
'assam'				:'./state_pics/assam.jpg' ,\
'bihar'				:'./state_pics/bihar.jpg' ,\
'chhattisgarh'		:'./state_pics/chhattisgarh.jpg' ,\
'goa'				:'./state_pics/goa.jpg' ,\
'gujarat'			:'./state_pics/gujarat.jpg' ,\
'haryana'			:'./state_pics/haryana.jpg' ,\
'himachal pradesh'	:'./state_pics/himachalpradesh.jpg' ,\
'jammu and kashmir'	:'./state_pics/jammuandkashmir.jpg' ,\
'jharkhand'			:'./state_pics/jharkhand.jpg' ,\
'karnataka'			:'./state_pics/karnataka.jpg' ,\
'kerala'			:'./state_pics/kerala.jpg' ,\
'madya pradesh'		:'./state_pics/madyapradesh.jpg' ,\
'maharashtra'		:'./state_pics/maharashtra.jpg' ,\
'manipur'			:'./state_pics/manipur.jpg' ,\
'meghalaya'			:'./state_pics/meghalaya.jpg' ,\
'mizoram'			:'./state_pics/mizoram.jpg' ,\
'nagaland'			:'./state_pics/nagaland.jpg' ,\
'orissa'			:'./state_pics/orissa.jpg' ,\
'punjab'			:'./state_pics/punjab.jpg' ,\
'rajasthan'			:'./state_pics/rajasthan.jpg' ,\
'sikkim'			:'./state_pics/sikkim.jpg' ,\
'tamil nadu'		:'./state_pics/tamilnadu.jpg' ,\
'tripura'			:'./state_pics/tripura.jpg' ,\
'uttaranchal'		:'./state_pics/uttaranchal.jpg' ,\
'uttar pradesh'		:'./state_pics/uttarpradesh.jpg' ,\
'west bengal'		:'./state_pics/westbengal.jpg' ,\
'andaman and nicobar islands':'./state_pics/andamanandnicobarislands.jpg' ,
'chandigarh'		:'./state_pics/chandigarh.jpg' ,\
'dadar and nagar haveli':'./state_pics/dadarandnagarhaveli.jpg' ,\
'daman and diu'		:'./state_pics/damananddiu.jpg' ,\
'delhi'				:'./state_pics/delhi.jpg' ,\
'lakshadeep'		:'./state_pics/lakshadeep.jpg' ,\
'pondicherry'		:'./state_pics/pondicherry.jpg' }

# DB Connection
con = sqlite3.connect('sample.db')
c = con.cursor()

# SES | Mail connection
#s = smtplib.SMTP("email-smtp.us-east-1.amazonaws.com")
s = smtplib.SMTP("ses-smtp-prod-335357831.us-east-1.elb.amazonaws.com")
s.starttls()
from ses_cred import ses_cred as ses
user_name = ses.cred['user']
user_pswd = ses.cred['pswd']
s.login(user_name,user_pswd)

@route('/new', method='GET')
def new_info():
	if request.GET.get('save','').strip():
		
		new_first_name = request.GET.get('first_name').strip()
		new_last_name = request.GET.get('last_name').strip()
		new_email = request.GET.get('email').strip()
		new_state = request.GET.get('state').strip()
		get_pic = state_pics[new_state]
#		Table schema
#		CREATE TABLE userdb1 (first_name char(30), last_name char(30) ,email varchar(50), pri_state char(30) , sec_state char(30), primary key (email, pri_state) )
		c.execute("insert into dw_user (first_name,last_name,email,pri_state) values (?,?,?,?)",(new_first_name, new_last_name, new_email, new_state))
		con.commit()
		c.close()
		
		sender='mail@whenisdryday.in'
		fname=new_first_name
		email=new_email
		state=new_state
		message = """From: Dry Day <tequila@whenisdryday.in>
		To: %s <%s>
		Subject: Tomorrow is dry day
		This is a test e-mail message.
		LETS HAVE A TEQUILA
		"this is the image location %s
		Tomorrow is a dry day in %s
		""" %(fname,email,get_pic,state)
		s.sendmail(sender, email, message)
		print "Successfully sent email"
		
		return template('success.tpl')
	else:
		return template('new_user.tpl')

@route('/list')
def todo_list():
	con = sqlite3.connect('sample.db')
	c = con.cursor()
	c.execute("select * from dw_user")
	result = c.fetchall()
	c.close()
	return template('make_table',rows=result)

debug(True) #not in production. same for reloader=True

run(host='localhost', port=8080, reloader=True)
