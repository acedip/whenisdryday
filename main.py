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

con = sqlite3.connect('sample.db')
c = con.cursor()

def check_dryday():
	c.execute("SELECT a.first_name,a.email,a.state \
	FROM userdb1 AS a \
	INNER JOIN dryday AS b \
		ON a.state=b.state \
	WHERE  drydate=date('now','+1 day')"\
	)
	result = c.fetchall()
	c.close()
	return tuple (result)

def users_dryday(args):
	for rows in args:
		print (rows)
		sender='anirudh@whenisdryday' #irrelevant 
		fname=rows[0] #first name
		email=rows[1] 
		state=rows[2] 
		# Test mail. The loop fails here as the mail service fails.
		message = """From: From Person <from@fromdomain.com>
		To: To Person <to@todomain.com>
		Subject: Tomorrow is dry day
		
		Hi %s
		This is a test e-mail message.
		Tomorrow is a dry day in %s
		""" %(fname,state)

		smtpObj = smtplib.SMTP('localhost')
		smtpObj.sendmail(sender, email, message)
		print "Successfully sent email"

users_dryday(check_dryday())


