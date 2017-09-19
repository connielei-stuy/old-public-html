#!/usr/bin/python
print "content-type: text/html\n"
print ""

import cgi
import cgitb
import os

cgitb.enable()

def getGames(username):
        games = []
        for file in os.listdir("data/games"):
                if file.find(username) != -1:
                        games.append(file)
        return games

def writeFile(output, filename):
        f = open(filename, 'w')
        f.write(output)
        f.close()

def getUser(params):
        return params['username'].value

def getOpponent(params):
        return params['opponent'].value

def generateData(user, opponent):
        data = ""
        data += user + "\n"
        data += "0\n"
        data += str([" "]*7) + "\n"
        data += opponent + "\n"
        data += "0\n"
        data += str([" "]*7) + "\n"
        data += str([[" "]*15]*15)
        return data

def generateFilename(user, opponent):
        return "data/games/" + user + "_" + opponent + ".txt"

def makeGame():
        params = cgi.FieldStorage()
        user = getUser(params)
        opponent = getOpponent(params)
        games = getGames(user)
        filename1 = user + "_" + opponent + ".txt"
        filename2 = opponent + "_" + user + ".txt"
        #if filename1 in games or filename2 in games:
        print "<p>This game already exists.</p>"
        #else:
        data = generateData(user, opponent)
        filename = generateFilename(user, opponent)
        writeFile(data, filename)
        print '<meta http-equiv="refresh" content="0;url=updates.py?username=' + user + '&opponent=' + opponent + '"/>'

makeGame()



