#!/usr/bin/python
from multiprocessing.connection import Listener
import cPickle as pickle
import threading
import Queue
import boto.ses
import datetime
import unirest
import sys

gMail=boto.ses.connect_to_region('')
sUser=''
sPswd=''
sSid=''

queue= Queue.Queue()

def SendMsgThread():
	"""
	Sends the actual email.
	Reads the email content from the queue.
	"""
	while 1:
		dMsg=queue.get() # This call is blocking when there is no email to be sent.
		dMsg=pickle.loads(dMsg)
#		print dMsg
		ferrlog = './src/log/postserver_error.log'
		flog = './src/log/postserver.log'		
		vMailTS = str(datetime.datetime.now())
		print "now trying to post ",dMsg['id']
		if dMsg['id']=='sms':
			try:
				response = unirest.get("http://cloud.smsindiahub.in/vendorsms/pushsms.aspx?user="+sUser+"&password="+sPswd+"&msisdn="+str(dMsg['phone'])+"&sid="+sSid+"&msg="+dMsg['sms']+"&fl=0")
				print "SMS successfully sent to sms india hub\n"
				fs=open(flog,'a')
				print >> fs, "SMS successfully sent to sms india hub\n", vMailTS, dMsg['phone'], dMsg['state']
				fs.close()
			except:
				allerror = sys.exc_info()[0]
				print "error in posting sms to sms india hub\n"
				fe=open(ferrlog,'a')
				print >> fs, "error in posting sms to sms india hub\n", vMailTS, dMsg['phone'], dMsg['state'],allerror
				fe.close()
				pass
		if dMsg['id']=='email':
			try:
				gMail.send_email(dMsg['from'],dMsg['subject'],dMsg['body'],dMsg['to'],format='html')
				print "email successfully sent to SES\n"
				fs=open(flog,'a')
				print >> fs, "email successfully sent to SES\n", vMailTS, dMsg['to'], dMsg['state']
				fs.close()
			except:
				allerror = sys.exc_info()[0]
				print "error in posting email to SES\n"
				fe=open(ferrlog,'a')
				print >> fs, "error in posting email to SES\n", vMailTS, dMsg['to'], dMsg['state'],allerror
				fe.close()
				pass

def listenOnPort(listener,connTCP):
	"""
	New thread created for every TCP connection that is established.
	This thread posts the msg into the queue, which is read by SendMsgThread for sending the actual email.
	"""
	print 'connection accepted from', listener.last_accepted
	msg= connTCP.recv()
	queue.put(msg)
	print queue.qsize()
	#connTCP.close()
	#listener.close()

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'

#Create the thread for sending Email
tMail= threading.Thread(target=SendMsgThread)
tMail.start()

listener = Listener(address, authkey='')
while True:
	connTCP=listener.accept()
	# Whenever a new connection is made, create a separate thread to handle it.
	# Then continue listening for connections on the port.
	t= threading.Thread(target=listenOnPort, args= (listener,connTCP))
	t.start()
listener.close() # This line is not expected to be executed since server should run forever
