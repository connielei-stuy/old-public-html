#!/usr/bin/python
print "Content-type: text/html\n"
print ""

import cgi
import cgitb
import hashlib

cgitb.enable()

def getUser(params):
        return params['user'].value

def getPassword(params):
        return params['password'].value

def hasher(s):
    return hashlib.sha256(s).hexdigest()

def checkCreds(params):
        user = getUser(params)
        password = getPassword(params)

        f = open("data/users.csv", 'r')
        data = f.readlines()

        users = []
        passwords = []
        for pair in data:
                pair = pair.split(",")
                users.append(pair[0].strip('\n'))
                passwords.append(pair[1].strip('\n'))

        return user in users and hasher(password) == passwords[users.index(user)]

def login():
        params = cgi.FieldStorage()
        username = getUser(params)
        if checkCreds(params):
                print '<meta http-equiv="refresh" content="0;url=main.py' + '?username=' + username + '"/>'
        else:
                print "<p>Your login information was incorrect. Please go back and try again.</p>"

login()


