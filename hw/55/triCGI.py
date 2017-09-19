#!/usr/bin/python
print "Content-type: text/html\n"
print ""

import cgi
import cgitb
from math import sqrt

def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

#cgitb.enable()

def perimeter(a,b,c):
  return a+b+c

def area(a,b,c):
  s = perimeter(a,b,c) / 2
  try:
    return sqrt(s*(s-a)*(s-b)*(s-c))
  except:
    return -1

def display():


  print "<p>Sides: " + str(a) + ", " + str(b) + ", " + str(c) + "</p>"
  if A == -1:
    print "<p>This triangle does not exist</p>"
  else: 
    print "<p>Area: " + str(A) + "</p>"
    print "<p>Perimeter: " + str(P) + "</p>"

# HTML
header = """
<!DOCTYPE html>
<html>
<head></head>
<body>
"""

footer = """
</body>
</html>
"""

print header
display()
print footer

