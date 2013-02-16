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

