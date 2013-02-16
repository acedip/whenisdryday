#!/usr/bin/python

import sqlite3
from bottle import route, run, debug, template, request

@route('/new', method='GET')
def new_info():
	if request.GET.get('save','').strip():
		
		new_first_name = request.GET.get('first_name').strip()
		new_last_name = request.GET.get('last_name').strip()
		new_email = request.GET.get('email').strip()
		new_state = request.GET.get('state').strip()
	
		con = sqlite3.connect('sample.db')
		c = con.cursor()
		c.execute("insert into userdb1 (first_name,last_name,email,state) values (?,?,?,?)",(new_first_name, new_last_name, new_email, new_state))
		con.commit()
		c.close()
		return template('success.tpl')
	else:
		return template('new_user.tpl')


debug(True) #not in production. same for reloader=True

run(host='localhost', port=8080, reloader=True)

