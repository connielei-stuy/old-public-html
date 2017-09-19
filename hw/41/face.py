#!/usr/bin/python
print "content-type: text/html\n"
print ""

import random

print "<html>"
print '<pre> \n<body style="text-align:center">'

def choose(L):
         return L[random.randrange(len(L))]
print "<t><b><p> Bunny Commander </p><b>"
def build():
    top = "l w i o x v n m |".split(" ")
    headl =[ "[","{","|","T","!"]
    headr = ["]","}","|","T","!"]
    eyes = ["'",'"',"0","O","o","=","x","*","~","z","-","_","`","^","v"]
    mouth = ["-","_","=","~","o","O","0","w","y","v","."]
    string = (choose(top) * 5) + "\n"
    string = string + choose(headl) + choose(eyes) + " "
    string = string + string[7]
    string += headr[headl.index(string[6])]
    string += "\n"
    string += " " * 2 + choose(mouth) + "  "
    print string

build()

print "<t><b><p> Bunny Army </p><b>"

print " ()_() \n (O.o) \n'(" + '")(")' + "'"
print ""
print " ()_() \n (o.O) \n'(" + '")(")' + "'"
print ""
print " ()_() \n (O.O) \n'(" + '")(")' + "'"
print ""
print " ()_() \n (o.o) \n'(" + '")(")' + "'"
print ""
print " ()_() \n(--.--)\n'(" + '")(")' + "'"
print ""
print " ()_() \n(==.==)\n'(" + '")(")' + "'"
print ""
print " ()_() \n (^.^) \n'(" + '")(")' + "'"

print "<t></body>\n</pre>\n</html>"
