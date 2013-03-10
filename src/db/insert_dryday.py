#!/usr/bin/python

#	whenisdryday.in is a email subscription based service to inform users 
#	when is a dry day in India.
#	Copyright (C) 2013  Anirudh singh shekhawat shekhawat.anirudh@gmail.com
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, version 3 of the License
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details http://www.gnu.org/licenses

import sqlite3
from bottle import route, run, debug, template, request

# DB Connection
con = sqlite3.connect('sample.db')
# Table Name
sWUser = 'userdb1' #dw_user
sWDryDay = 'dryday' #dw_dryday

@route('/insertdryday', method='GET')
def insert_dry_days():
	if request.GET.get('save','').strip():
		
		new_drydate = request.GET.get('drydate').strip()
		new_state = request.GET.get('state').strip()
	
#		Table schema
#		CREATE TABLE dryday (dw_dryday integer, state char(30) , primary key(dw_dryday,state) )
		gDBConn = con.cursor()
		gDBConn.execute("insert into "+sWDryDay+" (drydate,state) values (?,?)",(new_drydate, new_state))
		con.commit()
		gDBConn.close()
		return template('insert_dryday.tpl')
	else:
		return template('insert_dryday.tpl')

@route('/listdryday')
def list_all_drydays():
	gDBConn = con.cursor()
	gDBConn.execute("select * from "+sWDryDay+"")
	result = gDBConn.fetchall()
	gDBConn.close()
	return template('make_table',rows=result)

@route('/listuser')
def list_all_users():
	gDBConn = con.cursor()
	gDBConn.execute("select * from "+sWUser+"")
	result = gDBConn.fetchall()
	gDBConn.close()
	return template('make_table',rows=result)

debug(True) #not in production. same for reloader=True

run(host='localhost', port=8081, reloader=True)

