#!/usr/bin/python

import cgi
import cgitb

rawInput = cgi.FieldStorage()
# this always returns
# FieldStorage(None, None, [])

name = ["_"]

def refine():
    inputCords = {}
    for kV in rawInput:
        inputCords[kV] = rawInput[kV].value
        if "_" in kV:
            name[0] = [kV]
    return inputCords

inputCords = refine()
# this creates a dictionary of the inputted letters
# {'12,8': 'e', '11,8': 'd', '10,8': 'c', '9,8': 'b', '8,8': 'a'}

def fileOpen(filename):
    inStream = open(filename,"r")
    Input = inStream.readlines()
    inStream.close()
    return Input

rawData[7] = fileOpen(name[0]+".txt")

def dictionary(tableList):
    tableDict = {}
    for row in tableList:
        r = tableList.index(row) + 1
            for cell in row:
                n = row.index(cell) + 1
                tableDict[str(n) + "," + str(r)] = cell
    return tableDict

preTable = dictionary(rawData)

def merge(dict1,dict2):
    newDict = dict1
    for cords in dict2:
        newDict[cords] = dict2[cords]
    return newDict

postTable = merge(preTable,inputCords)

def sort(cords):
    x = []
    y = []
    for coordinate in cords:
        x += [int(coordinate.split(",")[0])]
        y += [int(coordinate.split(",")[1])]
    finalCords = []
    if min(x) == max(x):
        x = min(x)
        tempy = min(y)
        while tempy <= max(y):
            finalCords += [[x,tempy]]
            tempy += 1
    if min(y) == max(y):
        y = min(y)
        tempx = min(x)
        while tempx <= max(x):
            finalCords += [[tempx,y]]
            tempx += 1
    return finalCords

orderedCords = sort(inputCords)
# this creates a list of lists with the cords
# input sort(inputCords) to recieve
# [[8, 8], [9, 8], [10, 8], [11, 8], [12, 8]]

def borderCheck(square):
    newSquare = []
    for direction in square:
        if direction[0] <16 and direction[1] <16 and \
           direction[0] > 0 and direction[1] > 0:
            newSquare += [direction]
    return newSquare
# this makes sure that any cords inputted aren't outside of the playing table
# input borderCheck([[0,1],[1,2],[1,0],[2,1]]) to recieve
# [[1,2],[2,1]]

def connectCheck(cords):
    connectCords = []
    for coordinate in cords:
        left = [coordinate[0] - 1,coordinate[1]]
        right = [coordinate[0] + 1,coordinate[1]]
        up = [coordinate[0],coordinate[1] + 1]
        down = [coordinate[0],coordinate[1] - 1]
        tempCords = borderCheck([left,right,up,down])
        for coordinate in tempCords:
            if not (coordinate in cords and coordinate in connectCords):
                connectCords += [coordinate]
    return connectCords
# you will always input the orderedCords
# input connectCheck([[8, 8], [9, 8], [10, 8], [11, 8], [12, 8]]) to recieve
# [[7, 8], [9, 8], [8, 9], [8, 7], [8, 8], [10, 8], [9, 9], [9, 7], [11, 8], \
# [10, 9], [10, 7], [12, 8], [11, 9], [11, 7], [13, 8], [12, 9], [12, 7]]

adjacentCords = connectCheck(orderedCords)

def stringfy(cords):
    return str(cords[0]) + "," + str(cords[1])
# this switches the cords into strings
# format [n,r] becomes "n,r"
# input stringfy([7,8]) to recieve
# '7,8'

def filled(connectCords):
    filledCords = []
    for cords in connectCords:
        temp = stringfy([cords[0],cords[1]])
        if preTable[temp] != " ":
            filledCords += [cords]
    return filledCords
# you will always input the adjacentCords
# input wordBranch(adjacentCords) to recieve
# [[9,8],[8,7]]
# this completely depends on whether those coordinates have a letter attached
filledCords = filled(adjacentCords)

def seperateBranch(inputCords,filledCords):
    if filledCords == [] and [8,8] in inputCords:
        word = ""
        for cords in inputCords:
            word += postTable[stringfy(cords)]
        return [word]
    wordsList = []
    # this will hold all the branched words created
    for coordinate in filledCords:
        # for every single letter attached to the word you put down, this checks
        # to see the possible horizontal and vertical words created
        word = postTable(stringfy(coordinate))
        # this acts as the base letter to build off of, so if [8,8] were equal to
        # "e" stored in the postDictionary(the possible final dictionary), we will
        # add letters to the end and front of "e"
        rcords = coordinate
        # stands for right coordinate, meaning from [8,8], we check the parallel line y = 8
        # so we check [9,8] [10,8] [11,8] ... so on as long as there are letters present
        while rcords[0] <= 15 and postTable(stringfy(rcords)) != " ":
            word += postTable[stringfy(rcords)]
            # since the right is the end of the word, we add the letters to the back
            # so if it were an "e" base, it could be "ec"
            rcords[0] = [rcords[0] + 1]
            # this changes [8,8] into [9,8]
        lcords = coordinate
        # stands for left coordinate, meaning from [8,8], we check the same parallel line y = 8
        # so we check [7,8] [6,8] [5,8]
        while lcords[0] >= 1 and postTable(stringfy(lcords)) != " ":
            word = postTable(stringfy(lcords)] + words
            # we continued to use the word from before so it could potentially be "ect"
            # and we might do "s" + "ect" to get "sect
            lcords[0] = [lcords[0] - 1]
            # this subtracts the value, changes [8,8] to [7,8]
        if word != postTable(stringfy(cords)) and not word in wordsList:
            # this checks to make sure the word isn't a single letter, which it never should be
            # but just in case, and also checks to see if the word isn't already in the list, saves
            # time latter
            wordsList += [word]
        # then we repeat the entire process but for the vertical possible words
        word = tableDict(stringfy(coordinate))
        # this resets the base letter 
        dcords = coordinate
        while dcords[1] <= 15 and postTable(stringfy(dcords)) != " ":
            word += postTable[stringfy(rcords)]
            dcords[1] = [dcords[1] + 1]
        ucords = coordinate
        while ucords[1] >= 1 and postTable(stringfy(ucords)) != " ":
            word = postTable(stringfy(ucords)] + words
            ucords[1] = [ucords[1] - 1]
        if word != postTable(stringfy(cords)) and not word in wordsList:
            wordsList += [word]
    return wordsList

words = seperateBranch(orderedCords,filledCords)

def checkWords(words):
    n = True
    for word in words:
        if not word in "COMPLETE DICTIONARY":
            n = False
    return n

yellow=[[4,1],[12,1],[15,4],[1,4],[4,15],[12,15],[1,12],[15,12]]
blue=[[2,3],[2,13],[3,2],[3,5],[3,14],[3,11],[5,3],[5,7],[5,9],[5,13],[7,5],[7,11],\
      [14,3],[14,13],[13,2],[13,5],[13,14],[13,11],[11,3],[11,7],[11,9],[11,13],[9,5],[9,11]]
red = [[2,6],[2,10],[4,8],[6,2],[6,14],[8,4],[8,12],[10,14],[10,2],[14,6],[14,10],[12,8]]
green=[[1,7],[1,9],[4,4],[4,12],[6,6],[6,10],[7,1],[7,15],[9,1],[9,15],[10,6],[10,10],[15,7],[15,9],[12,4],[12,12]]
colors = yellow + blue + red + green + [[8,8]]

def cellData(cords,value):
    start = "\t\t<td width='50px' height='50px'"
    ending = "\n\t\t</td>\n"
    form = value
    if value == " ":
        form = "\n\t\t\t<input type ='text' name='" + cords + "'size='1'maxlength='1'>"
    if [n,r] in colors:
        cords=[n,r]
        if cords in yellow:
            special = "bgcolor='yellow'>"
            return start + special + form + ending
        elif cords in red:
            special = "bgcolor='red'>"
            return start + special + form + ending
        elif cords in green:
            special = "bgcolor = 'green'>"
            return start + special + form + ending
        elif cords == [8,8]:
            special = "bgcolor = 'purple'>"
            return start + special + form + ending
        elif cords in blue:
            special = "bgcolor='blue'>"
            return start + special + form + ending
    else:
        special = ">"
        return start + special + form + ending

def table():
    html = "<html>\n <form name = 'input' method ='POST' action ='updateWord.py'>\n\
<table border='1'align='center'>\n"
    r = 1
    while r < 16:
            tableRow = "\t<tr>\n"
            n = 1
            while n != 16:
                cords = stringfy([n,r])
                tableRow += cellData(cords,postTable[cords])
                n += 1
            r += 1
            tableRow += "\t</tr>\n"
            html += tableRow
        html += "</table>\n</html>"
    return html

n = checkWords(words)

def reBuild():
    if n:
        return table()
    else:
        "refresh page"

html = reBuild()

def choice():
    if n:
        return postTable

a = choice()

def fileWrite(output,filename):
    outStream = open(str(filename),"w")
    outStream.write(output)
    outStream.close()

fileWrite(html,name[0] +".html")
fileWrite(a,name[0] + ".txt")

