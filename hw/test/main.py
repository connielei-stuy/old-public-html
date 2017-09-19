#!/usr/bin/python

print "Content-type: text/html\n"
print ""

import cgi
import cgitb
import os

cgitb.enable()

def getUsers():
        f = open("data/users.csv", 'r')
        data = f.readlines()
        f.close()

        users = []
        for pair in data:
                pair = pair.split(',')
                users.append(pair[0].strip('\n'))

        return users

def getUsername(params):
        return params['username'].value

def chooseUsers(users, currentUser):
        users.remove(currentUser)
        return users

def getButton(user):
        return user + "\n<input type='radio' name='opponent' value='" + user + "'>\n<br>"

def displayUsers(params):
        currentUser = getUsername(params)
        users = getUsers()
        users = chooseUsers(users, currentUser)
        print "<form action='makeGame.py' method='POST'>"
        print "Current user<br>"
        print currentUser + "\n<input type='radio' name='username' value='" + currentUser + "' checked='checked'>\n<br><br>"
        print "Opponents<br>"
        for user in users:
                if user == users[0]:
                        print user + "\n<input type='radio' name='opponent' value='" + user + "' checked='checked'>\n<br>"
                else:
                        print getButton(user)
        print "<br>\n<input type='submit' value='Play!'>"


def getGames(username):
        games = []
        for file in os.listdir("data/games"):
                if file.find(username) != -1:
                        games.append(file)
        return games
def displayGames(params):
        print "<br><br>"
        print "Current games<br>"
        games = getGames(getUsername(params))
        for game in games:
                print game + "<br>"

def main():
        params = cgi.FieldStorage()
        displayUsers(params)
        displayGames(params)

main()

