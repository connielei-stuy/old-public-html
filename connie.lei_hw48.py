"""
Connie Lei
IntroCS2 pd8
2016-05-16
HW48 - Almost Crunching Real Numbers

"""

def fileOpen(filename):
    inStream = open(str(filename),"r")
    Input = inStream.readlines()
    inStream.close()
    return Input

fileInfo = fileOpen("data_SAT2012.csv")

def specialCase(statement):
    temp = statement.split(',')
    temp[1:3] = [temp[1]+","+temp[2]]
    return temp

def listifyRow(rowInput):
    if '"' in rowInput:
        return specialCase(statement)
    else:
        return rowInput.split(',')
    
def htmlRow(rowList):
    tableRow = "\n\t\t<tr>"
    for data in rowList:
        tableRow += "\n\t\t\t<td>"
        tableRow += data
        tableRow += "</td>"
    tableRow += "\n\t\t</tr>"
    return tableRow

def genTable(dataInput):
    htmlString = "<!DOCTYPE html> \n<html>\n\t<table border = '1' align = 'center'>\n"
    tableInfo = ""
    for row in dataInput:
        tableInfo += htmlRow(row)
    htmlString += tableInfo
    htmlString += "\n\t</table>\n"
    htmlString += "<p> This is a table of the 2012 NYC SAT data of all schools from 2012. It also shows the mean of all over</p>"
    htmlString += "\n</html>"
    return htmlString

htmlString = genTable(fileInfo)

def fileWrite(output,filename):
    outStream = open(str(filename),"w")
    outStream.write(output)
    outStream.close()

# fileWrite(htmlString,"statsSAT.html")
