#!/usr/bin/python
print "Content-type: text/html\n"
print ""

import cgi
import cgitb
from math import sqrt

cgitb.enable()

def perim(a,b,c):
  return a + b + c

def check(a,b,c):
  lengths = [a,b,c]
  n = True
  for sidelength in lengths:
    if sum(lengths) - sidelength < sidelength:
      n = False
  return n

def area(a,b,c):
  s = perim(a,b,c) / 2
  if check(a,b,c):
    return str(sqrt(s*(s-a)*(s-b)*(s-c)))
  else:
    return "This triangle does not exist."

def display():
  params = cgi.FieldStorage()
  a = float(params['a'].value)
  b = float(params['b'].value)
  c = float(params['c'].value)
  A = area(a,b,c)
  P = perim(a,b,c)
  print "<p>Sides: " + str(a) + ", " + str(b) + ", " + str(c) + "</p>"
  print "<p>Area: " + A + "</p>"
  print "<p>Perimeter: " + str(P) + "</p>"

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

