"""
Team Gillei -- Connie Lei & Gilvir Gill
IntroCS2 pd8
HW22 -- Further Explorations in Toy_Encryption (Labwork)
2016-03-28
"""
###-----Function for Testing Code---###
def test(fxn,expected): #put the function and the expected output
    print fxn + " ,Expected: " + str(expected)
    if str(fxn) == str(expected):
        print "Correct!"
    else:
        print "Wrong!"



print '1. rot13Chr-Takes a single letter string and returns its rot13 value'

""" Connie's Version """

# Basically you convert the values and then if the number is near the end of the
# alphabet, then you subtract 13. If it is at the beginning of the alphabet, you
# add 13.

def rot13Chr1(ch):
	number = ord(ch)
	if (number < 78 and number > 64) or (number < 110 and number > 96):
		return chr(number + 13)
	else:
		return chr(number - 13)

""" Gilvir's Version """

# simplifies each expression to a value between 1 and 26 (0 equals 26 in this case).
# Then modulos the addition. For example if the number is 20, then add 13 to get 33.
# Then 33 % 26 is the 7th letter. After all of this, add back the difference.
		
def rot13Chr2(ch):
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

# 2. Swap your rot13Chr with the code below. Add descriptive comments that explain how
# this function works. The rest of your code should remain functional after replacing
# one working function with another. That is the beauty of modular design.

def rot13Chr(ch):
            # This checks to see if it is A or a and then sets the difference if it is an uppercase
            # to 65 or 97.
            if ch.upper()==ch:
                offset = ord('A')  #65
            else:
                offset = ord('a')  #97
            # The character is converted into a number, then 13 is added. You subtract the beginning
            # so that you a number that is 13 positions after and to ensure that you don't go over the
            # limit. If you have 27, then you need to subtract 26 hence the remainder. Then you added
            # the difference to the beginning of the alphabet. 
            return chr( (ord(ch)+13-offset) % 26  + offset ) 

#test cases
test(rot13Chr1('B'),'O')
test(rot13Chr('b'),'o')
test(rot13Chr('B'),'O')
test(rot13Chr('b'),'o')

print '2. printEmAll(): Prints all letters of the alphabet'

def printEmAll():
    counter = ord('A')
    max_char = ord('Z')
    while counter <= max_char:
        print "%s <-> %s" % (chr(counter),rot13Chr(chr(counter)))
        counter += 1
    counter = ord('a')
    max_char = ord('z')
    while counter <= max_char:
        print "%s <-> %s" % (chr(counter),rot13Chr	(chr(counter)))
        counter += 1
#test
printEmAll()


print '3. rot13Wrd(word). Takes string input and returns rot13 encoding using the rot13Chr function'

def rot13Wrd(word): #done by generating a second string and removing from the other
    ans = ''
    while word != '': #keep running the while loop until all parts of the word have been transferred to the answer variable.
        ans += rot13Chr(word[0])
        word = word[1:]
    return ans
#test cases
test(rot13Wrd("JABBERWOCKY"),"WNOOREJBPXL")
test(rot13Wrd("WNoOREJBPXl"),"JAbBERWOCKy")

def rot13(phrase):
    string=''
    end = len(phrase)
    while len(string) < end:
        string += rot13Wrd(phrase[:phrase.index(" ")]) + " "
        phrase = phrase[phrase.index(" "):]
    return string

print rot13("Justin Bieber")
