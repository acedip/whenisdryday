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
from bottle import route, run, debug, template, request
from email.mime.text import MIMEText
from multiprocessing.connection import Client
import cPickle as pickle
import errno, socket
import sys

# DB Connection
con = sqlite3.connect('./src/db/dryday.db')
#con = sqlite3.connect('./src/db/test.db')
# sqlite3 unicode to string conversion
con.text_factory = str
# Table Name
sWUser = 'dw_user'
sWUserLive = 'dw_user_live'
sWDryDay = 'dw_dryday'

#execute("create table dw_dryday (state text, reason text, dryday text)")
#execute("create table dw_user (name text, email text, state text, phone integer)")
#execute("create table dw_user_live (name text, email text, state text, phone integer)")

def fPostToServer(email_html,dUserInfo,sUserNxtDryDayDtl):
	gMailTS = datetime.datetime.now()
	address = ('localhost',6000)
	connTCP = Client(address, authkey='')
	sSubject = ''+sUserNxtDryDayDtl['msg']+' in '+dUserInfo['state']+''
	sMe = 'tequila@whenisdryday.in'
	dMsg = {'id':'email', 'from':sMe, 'subject': sSubject, 'body': email_html ,'to':dUserInfo['email'],'state':dUserInfo['state']}
	connTCP.send(pickle.dumps(dMsg))
	connTCP.close()
	print str(gMailTS), "EMAIL successfully sent to the post office server"
	sSMS = ''+sUserNxtDryDayDtl['msg']+' in '+dUserInfo['state']+'. '+sUserNxtDryDayDtl['day1']+' '+sUserNxtDryDayDtl['date1']+' '+sUserNxtDryDayDtl['month1']+''
	dMsg = {'id':'sms', 'sms':sSMS, 'phone':dUserInfo['phone'],'state':dUserInfo['state']}
	connTCP = Client(address, authkey='')
	connTCP.send(pickle.dumps(dMsg)) 
	connTCP.close()
	print str(gMailTS), "SMS successfully sent to the post office server"

def check_dryday():
	gDBConn = con.cursor()
	gDBConn.execute("SELECT a.name, a.email, a.phone, a.state, b.drydate, c.drydate\
	FROM "+sWUserLive+" AS a \
	INNER JOIN "+sWDryDay+" AS b ON a.state=b.state and b.drydate=date('now','+1 day')\
	LEFT JOIN "+sWDryDay+" AS c ON a.state=c.state and c.drydate=date('now','+2 day') \
	WHERE a.state NOT IN (SELECT state FROM "+sWDryDay+" WHERE drydate=date('now') )")
	tUserData = gDBConn.fetchall()
	gDBConn.close()
	return tuple (tUserData)

def fSuccessMail(dUserInfo,sUserNxtDryDayDtl):
	gDBConn = con.cursor()
	gDBConn.execute("select reason, drydate from "+sWDryDay+" where state = '"+dUserInfo['state']+"' and strftime('%Y',drydate)=strftime('%Y','now') order by drydate")
	sUserAllDryDay=tuple(gDBConn.fetchall())
	lStateBanner=('Maharashtra','Delhi','Tamilnadu','West Bengal')
	dStateBanner={'Maharashtra':'http://whenisdryday.in/bs/img/mail/tn1.jpg','Delhi':'http://whenisdryday.in/bs/img/mail/del1.jpg'\
		,'West Bengal':'http://whenisdryday.in/bs/img/mail/wb1.jpg','Tamilnadu':'http://whenisdryday.in/bs/img/mail/tn1.jpg'}
	return template ('./src/mail/dd_remind.tpl', dStateBanner=dStateBanner,lStateBanner=lStateBanner,sUserAllDryDay=sUserAllDryDay, dUserInfo=dUserInfo, sUserNxtDryDayDtl=sUserNxtDryDayDtl)

lUserFields= ['name', 'email', 'phone','state','DT1','DT2']

def fSendMail(tUserData):
	"""
	Email Sending
	fSuccessEmail called and fed into the MIME Text as msg
	msg is a list. with values like sender, subject etc
	Returns success if email sent
	"""
	for row in tUserData:
		dUserInfo = dict(zip(lUserFields,row))
		#Printing user fields from DB Output
		print dUserInfo
		gMailTS = datetime.datetime.now()
		''''
		sUserNxtDryDay=Converts dry day dates per user (from DB output) into python (checks for None as need only string) date format to get weekday, month etc.
		sUserNxtDryDayDtl=Stores Weekday,month to feed into email/sms title message 
		'''
		if dUserInfo['DT2']<>None:
			#DB Output converts to python date format
			sUserNxtDryDay={'DT1':time.strptime(dUserInfo['DT1'],'%Y-%m-%d')\
				,'DT2':time.strptime(dUserInfo['DT2'],'%Y-%m-%d')}
			#Email Message + Day 2 Dates
			sUserNxtDryDayDtl={'id':'main', 'msg':'Next 2 Days are Dry Days', 'day2':time.strftime('%A',sUserNxtDryDay['DT2'])\
			,'date2':time.strftime('%d',sUserNxtDryDay['DT2']), 'month2':time.strftime('%b',sUserNxtDryDay['DT2'])\
			#Day 1 Dates
			,'day1':time.strftime('%A',sUserNxtDryDay['DT1']), 'date1':time.strftime('%d',sUserNxtDryDay['DT1']), 'month1':time.strftime('%b',sUserNxtDryDay['DT1'])}
		else:
			#DB Output converts to python date format
			sUserNxtDryDay={'DT1':time.strptime(dUserInfo['DT1'],'%Y-%m-%d')}
			#Email Message + Day 1 Dates
			sUserNxtDryDayDtl={'id':'main', 'msg':'Tomorrow is Dry Day', 'day1':time.strftime('%A',sUserNxtDryDay['DT1'])\
			,'date1':time.strftime('%d',sUserNxtDryDay['DT1']), 'month1':time.strftime('%b',sUserNxtDryDay['DT1']),\
			'date2':"",'day2':"",'month2':""}
		email_html = (fSuccessMail(dUserInfo,sUserNxtDryDayDtl))
		print "trying to post to server", str(gMailTS), sUserNxtDryDayDtl
		try:
			fPostToServer(email_html,dUserInfo,sUserNxtDryDayDtl)
			flog='./src/log/main_to_post_sucess.log'
			sMsg=''+str(gMailTS)+' Name= '+dUserInfo['name']+' State= '+dUserInfo['state']+' Email= '+dUserInfo['email']+' and Phone= '+str(dUserInfo['phone'])+''
			f=open(flog,'a')
			print >> f, str(gMailTS), sMsg
			f.close()
			fMail1 = './src/mail/'+str(gMailTS)+'_'+dUserInfo['email']+'_'+dUserInfo['state']+'.html'
			f1=open(fMail1,'w')
			print >> f1, email_html
			f1.close()
		except socket.error, v:
			allerror = sys.exc_info()[0]
			gMailTS = datetime.datetime.now()
			print "error in sending to post office server", str(gMailTS)
			fsockerr = './src/log/main_to_post_error.log'
			sferr = ''+str(gMailTS)+' Name= '+dUserInfo['name']+' State= '+dUserInfo['state']+' Email= '+dUserInfo['email']+' and Phone= '+str(dUserInfo['phone'])+''
			f2=open(fsockerr,'a')
			print >>f2, sferr,allerror
			f2.close
		return 1

tUserData = check_dryday()

print tUserData

fSendMail(tUserData)
