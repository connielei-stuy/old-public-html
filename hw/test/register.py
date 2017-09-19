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

def getCheckPassword(params):
        return params['checkPassword'].value

def checkUserName(user):
        return user.isalnum() and len(user) > 3 and len(user) < 11

def checkPassword(p1, p2):
        return p1 == p2

def hasher(s):
    return hashlib.sha256(s).hexdigest()

def dupUserName(user):
        f = open("data/users.csv", 'r')
        data = f.readlines()
        f.close()

        users = []
        for pair in data:
                pair = pair.split(",")
                users.append(pair[0])

        return user in users

def createUser(username, password):
        f = open("data/users.csv", 'a')
        f.write(username + "," + password + "\n")
        f.close()

def register():
        params = cgi.FieldStorage()
        user = str(getUser(params))
        password1 = str(getPassword(params))
        password2 = str(getCheckPassword(params))                        else:
                                print "<p>Your passwords do not match. Please retype your password.</p>"
                else:
                        print "<p>Your username has already been taken. Please choose another username.</p>"
        else:
                print "<p>Your username must be alphanumeric and between 4 and 10 characters long.</p>"


register()

        if checkUserName(user):
                if not dupUserName(user):
                        if checkPassword(password1, password2):
                                createUser(user, hasher(password1))
                                print '<meta http-equiv="refresh" content="0;url=index.html"/>'

