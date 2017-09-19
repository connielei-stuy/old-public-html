#!/usr/bin/python
print "content-type: text/html\n"
print ""

import os

def fileOpen(filename):
    inStream = open(str(filename),"r")
    Input = inStream.readlines()
    inStream.close()
    return Input

def fileWrite(output,filename):
    outStream = open(str(filename),"w")
    outStream.write(output)
    outStream.close()

def environment(a):
    htmlString = ""
    for value in a:
        htmlString += "\nkey:\t"
        htmlString += str(value)
        htmlString += "\nvalue:\t"
        htmlString += str(a[value])
    return htmlString

fileWrite(environment(os.environ),"text.html")
