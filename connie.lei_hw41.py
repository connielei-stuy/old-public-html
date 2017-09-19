"""
Team --Connie Lei,Ryan Siu
IntroCS2pd8
HW41 -- ASCIIng About Your Visage
2016-05-05

1. common(L1,L2) takes 2 lists as input and returns a new list containing values common to both. Assumes no repeated values in either list.
e.g., common( [1,5,4,3,2] , [4,5,10,15] ) → [4,5]
2. alphabetize(names) takes a string of names, assumed to be in Last-First pairings, separated by commas, and returns an alphabetized list
of names with line breaks in string form. Summarize algorithm in a block comment preceding your function.
e.g., alphabetize( “Wayne,Bruce,Kent,Clark,Parker,Peter” ) → “Kent Clark\nParker Peter\nWayne Bruce”
"""

def alphabetize(names):
    newList = ""
    while len(names) != 0:
        newList += names[:names.find(",")]
        newList += " "
        print newList
        names = names[names.find(",")+1:]
        print names
        newList += names[:names.find(",")]
        newList += "\n"
        print newList
        names = names[names.find(",")+1:]
    newList += names

print alphabetize("Wayne,Bruce,Kent,Clark,Parker,Peter")
