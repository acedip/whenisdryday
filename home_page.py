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

#!/usr/bin/python

import sqlite3
from bottle import route, run, debug, template, request

con = sqlite3.connect('sample.db')
c = con.cursor()

@route('/new', method='GET')
def new_info():
	if request.GET.get('save','').strip():
		
		new_first_name = request.GET.get('first_name').strip()
		new_last_name = request.GET.get('last_name').strip()
		new_email = request.GET.get('email').strip()
		new_state = request.GET.get('state').strip()
#		Table schema
#		CREATE TABLE userdb1 (first_name char(30), last_name char(30) ,email varchar(50) primary key ,state char(30) not null)
		c.execute("insert into userdb1 (first_name,last_name,email,state) values (?,?,?,?)",(new_first_name, new_last_name, new_email, new_state))
		con.commit()
		c.close()
		return template('success.tpl')
	else:
		return template('new_user.tpl')

@route('/list')
def todo_list():
	con = sqlite3.connect('sample.db')
	c = con.cursor()
	c.execute("select * from userdb1")
	result = c.fetchall()
	c.close()
	return template('make_table',rows=result)

debug(True) #not in production. same for reloader=True

run(host='localhost', port=8080, reloader=True)

