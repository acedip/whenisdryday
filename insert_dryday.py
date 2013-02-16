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

#!/usr/bin/python

import sqlite3
from bottle import route, run, debug, template, request

@route('/insert', method='GET')
def new_info():
	if request.GET.get('save','').strip():
		
		new_drydate = request.GET.get('drydate').strip()
		new_state = request.GET.get('state').strip()
	
		con = sqlite3.connect('sample.db')
		c = con.cursor()
#		Table schema
#		CREATE TABLE dryday (drydate integer, state char(30) , primary key(drydate,state) )
		c.execute("insert into dryday (drydate,state) values (?,?)",(new_drydate, new_state))
		con.commit()
		c.close()
		return template('insert_dryday.tpl')
	else:
		return template('insert_dryday.tpl')

@route('/check')
def todo_list():
	con = sqlite3.connect('sample.db')
	c = con.cursor()
	c.execute("select * from dryday")
	result = c.fetchall()
	c.close()
	return template('make_table',rows=result)

debug(True) #not in production. same for reloader=True

run(host='localhost', port=8081, reloader=True)

