#!/usr/bin/python

#import psutil as p
import datetime
import subprocess 
import time

h='./src/log/homepage.log'
n='./src/log/n00b.log'
s='./src/log/postserver.log'
#m='./src/log/main.log'

fn=open(n,'a')
fs=open(s,'a')
p_server=subprocess.Popen('./src/post_server.py',stderr=fs)
fs.close()
vMailTS = str(datetime.datetime.now())
print >>fn,vMailTS,"post server started for the first time"
fn.close()
fh=open(h,'a')
p_home=subprocess.Popen('./home_page.py',stderr=fh)
fh.close()
vMailTS = str(datetime.datetime.now())
fn=open(n,'a')
print >>fn,vMailTS,"home page started for the first time"
fn.close()
home_cnt=1
post_cnt=1
#main_cnt=1

while True:
	time.sleep(1)
	if p_home.poll()!=None:
		fh=open(h,'a')
		p_home=subprocess.Popen('./home_page.py',stderr=fh)
		fh.close()
		vMailTS = str(datetime.datetime.now())
		fn=open(n,'a')
		print >>fn,vMailTS,"home page started for the ",home_cnt," time"
		fn.close()
		home_cnt+=1
	if p_server.poll()!=None:	
		fs=open(s,'a')
		p_server=subprocess.Popen('./src/post_server.py',stderr=fs,stdin=fs,stdout=fs)
		fs.close()
		vMailTS = str(datetime.datetime.now())
		fn=open(n,'a')
		print >>fn,vMailTS,"post office started for the ",post_cnt," time"
		fn.close()
		post_cnt+=1
"""	if time.strftime('%H',time.gmtime())==2:
		fm=open(m,'a')
		fm.close()
		vMailTS = str(datetime.datetime.now())
		print >>fn,vMailTS,"Main Process started for the ",main_cnt," time"
		main_cnt+=1
"""
