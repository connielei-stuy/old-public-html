"""
Team Solo -- Connie Lei (I don't know my partners' names....)
IntroCS2 pd8
HW23 -- Anslatingtray Englishway intoway Igpay Atinlay
2016-03-29

PIG LATIN RULES:
1. If the word begins with a vowel, add a way to the end.
2. If the word begins with consonant, and the second letter
   is not a vowel, move the first two letters to the end and
   add ay.
3. If the word begins with a consonant followed by a vowel,
   then move the first letter and add ay.   

OUTLINE:
There will be different functions that will check the the first letter,
then there will be another that will add way or ay to the end of the string
and there will be ones that move letters to the end.

DEVELOPMENT PLAN:
-adds the ay to string
-adds the way to string
-checks if starts with a vowel
-checks if the second one starts with a vowel
-moves letters

Guidelines:
Code mentioned in the development plan in order of simplicity.

DEVELOPMENT LOG:
11:39: addAY completed!
11:40: addWAY comepleted!
11:44: vowelCheck completed, changed to allow use for the second letter position
"""

def addAY(string):
    return string + "ay"

def addWAY(string):
    return string + "way"

def vowelCheck(string,pos):
    l = string[pos]
    return l == "a" or l == "e" or l == "i" or l == "o" or l == "u"

def move(string,length):
    return string[length:] + string[:length]

def trnsWrd(string):
    if vowelCheck(string,0):
        newS = addAY(string)
    elif vowelCheck(string,1):
        newS = addAY(move(string,1))
    else:
        newS = addAY(move(string,2))
    if newS == newS.lower():
        return newS
    else:
        return (newS.lower()).capitalize()

def trnsPhr(string):
    newS=""
    updS=string
    while updS.find != -1:
        newS += trnsWrd(updS[:updS.find(" ")]) + " "
        updS = updS[updS.find(" ")+1:]
    return newS

print trnsWrd("pigLatin"),trnsWrd("chararcter"),trnsWrd("Cat") #igLatinpay, aracterchay, Atscay
print trnsPhr("I am a cool person lio.") #Iway amway away oolcay ersonpay iolay.
