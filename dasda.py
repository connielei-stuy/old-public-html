def indexOf(s,x):
    testPosition=0
    while testPosition < len(s):
        if s[testPosition] == x:
            return testPosition
        testPosition += 1
    return -1 

s="Always strive and prosper"

