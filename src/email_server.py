#!/usr/bin/python

from multiprocessing.connection import Listener
import cPickle as pickle
import threading
import Queue

queue= Queue.Queue()

def SendEmailThread():
  """
  Sends the actual email.
  Reads the email content from the queue.
  """
  while 1:
    msg=queue.get() # This call is blocking when there is no email to be sent.
    msg= pickle.loads(msg)
    # We have the Email message over here. Put the code for sending it below
    #vMailTS = datetime.datetime.now()
    fMail = './mail_archives/success_mail/'+msg['To']+'.html'
    f=open(fMail,'w')
    print >> f, msg.as_string()
    f.close()
    print msg

def listenOnPort(listener,connTCP):
  """
  New thread created for every TCP connection that is established.
  This thread posts the msg into the queue, which is read by SendEmailThread for sending the actual email.
  """
  print 'connection accepted from', listener.last_accepted
  msg= connTCP.recv()
  queue.put(msg)
  connTCP.close()
  #listener.close()

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'

#Create the thread for sending Email
tMail= threading.Thread(target=SendEmailThread)
tMail.start()

listener = Listener(address, authkey='drydayiswhen')
while True:
  connTCP=listener.accept()
  # Whenever a new connection is made, create a separate thread to handle it.
  # Then continue listening for connections on the port.
  t= threading.Thread(target=listenOnPort, args= (listener,connTCP))
  t.start()
listener.close() # This line is not expected to be executed since server should run forever
