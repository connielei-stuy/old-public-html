#!/usr/bin/python
print "Content-Type:text/html\n"
print ""

"""
Connie Lei
IntroCS2 pd 8
HW#52 - GET Started Simply
2016-05-22
"""

import os
d = os.environ

def html(environment):
    htmlString = "<!DOCTYPE html>\n<html>"
    if d["QUERY_STRING"] == "":
        htmlString += "\n<p>No Query String</p>"
    else:
        htmlString += "\n<p>Query String:"
        htmlString += d["QUERY_STRING"]
        htmlString += "</p>\n"
    htmlString += "</html>"
    return htmlString

print html(d)

