#!/usr/bin/python

from bottle import Bottle, request, run
from bottle.ext import auth
from bottle.ext.auth.decorator import login
from bottle.ext.auth.social.facebook import Facebook
from pprint import pformat

facebook = Facebook('381968148649899','a8640c8ca796fe823fa3df7d63231b99','http://whenisdryday.in','anirudh')

app = Bottle()
plugin = auth.AuthPlugin(facebook)
app.install(plugin)


@app.route('/')
@login()
def home():
    user = auth.get_user(request.environ)
    return "Home page {}".format(pformat(user))


run(app=app, host='localhost', port='3333', debug=True)
