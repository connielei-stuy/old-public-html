#!/usr/bin/python
print "Content-Type:text/html\n"
print ""

import os
d = os.environ

def perm(a,b,c):
    return a + b + c

def herons(a,b,c):
    sp = perm(a,b,c)/2
    area = (sp * (sp - a) * (sp - b) * (sp - c)) ** 0.5
    return area

def html(environment):
    htmlString = "<!DOCTYPE html>\n<html>\n<p> Side Lengths:"
    sideLengths = environment["QUERY_STRING"]
    sideLengths = sideLengths.split("&")
    sides = []
    for length in sideLengths:
        a = length.split("=")
        sides += [int(a[-1])]
        htmlString += a[-1]
    htmlString += "\n Area:"
    htmlString += str(herons(sides[0],sides[1],sides[2]))
    htmlString += "\n Perimeter:"
    htmlString += str(perm(sides[0],sides[1],sides[2]))
    htmlString += "\n</p></html>"
    return htmlString

print html(d)


