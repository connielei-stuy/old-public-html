#!/usr/bin/python
print "Content-type: text/html\n"
print ""

import cgi
import cgitb

#cgitb.enable

x =  cgi.FieldStorage()

def rot13Chr(ch):
    ascii = ord(ch) #the ascii number value for ch
    if ascii >= ord('a'): #if its greater than 97 (the ascii value for a), subtract 97
        difference = ord('a')
    else: #otherwise, it's capital so only subtract the ascii value of A (65)
        difference = ord('A')
    ascii -= difference
    if ascii <= 0:
        ascii += 26
    rotated = (ascii+13)%26 #adds cyclicial nature using modulo 
    return chr(rotated+difference)

def rot13Wrd(word): #done by generating a second string and removing from the other
    ans = ''
    while word != '': #keep running the while loop until all parts of the word have been transferred to the answer variable.
        ans += rot13Chr(word[0])
        word = word[1:]
    return ans

def run():
	text = x["text"].value
	program = x["program"].value
	if program == "Reverse":
		text= text[::-1]
	else:
		text = rot13Wrd(text)
	if "bold" in x:
		text = "<b>" + text + "</b>"
	if "italics" in x:
		text = "<i>" + text + "</i>"
	if "underline" in x:
		text = "<u>" + text + "</u>"
	if "larger size" in x:
		text = "<font size = '12'>" + text +"</font>"
	print text

run()
