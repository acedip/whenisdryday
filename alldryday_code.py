#!/usr/bin/python

import sqlite3
from bottle import template
from collections import namedtuple, defaultdict

con=sqlite3.connect('./src/db/dryday.db')
c=con.cursor()
c.execute("select state, reason, drydate from dw_dryday where strftime('%Y',drydate)=strftime('%Y','now') order by 1,3")
record = namedtuple('record', ['state', 'reason', 'dd'])
statedatamap = defaultdict(list)
for row in map(record._make, c.fetchall()):
    statedatamap[row.state].append(row)
    #print statedatamap

f=open('./alldrydays.html','w')
print >> f , template('./alldrydays.tpl',smap = statedatamap)
f.close()
