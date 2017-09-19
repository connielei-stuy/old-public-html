"""
Connie Lei
IntroCS2 pd8
2016-05-18
HW49 -- How many numbers could a thinker crunch if a thinker could crunch numbers?

"""

def fileOpen(filename):
    inStream = open(str(filename),"r")
    Input = inStream.readlines()
    inStream.close()
    return Input

fileInfo = fileOpen("data_SAT2010.csv")

def tidyfy(listString):
    n = 0
    for string in listString:
        listString[n] = string.strip("\n")
        n += 1
    return listString

fileInfo = tidyfy(fileInfo)

def specialCase(statement):
    temp = statement.split(',')
    temp[1:3] = [temp[1]+","+temp[2]]
    if len(temp) > 6:
        temp[1:3] = [temp[1]+temp[2]]
    return temp

def updateList(listString):
    newList = []
    for string in listString:
        if '"' in string:
            newList += [specialCase(string)]
        else:
            newList += [string.split(",")]
    return newList

tableList = updateList(fileInfo)
  
def htmlRow(rowList):
    tableRow = "\n\t\t<tr>"
    for data in rowList:
        tableRow += "\n\t\t\t<td>"
        tableRow += data
        tableRow += "</td>"
    tableRow += "\n\t\t</tr>"
    return tableRow

htmlHead = "<!DOCTYPE html> \n<html>"
htmlMid = "\n<p> This is a table of the 2012 NYC SAT data of all schools from 2012. It also shows the mean of all overall average math, reading and writing scores as well as \
the average of overall SAT scores. It shows the highest and lowest average score. It inclues the total number of tests taken and the average taken of \
all schools.</p>\n"
htmlTail = "</html>"

def genTable(dataInput):
    tableInfo = "\n\t<table border = '1' align = 'center'>\n"
    for row in dataInput:
        tableInfo += htmlRow(row)
    tableInfo += "\n\t</table>\n"
    return tableInfo

def coloumn(position,totalList):
    tempList = totalList [1:]
    newList = []
    for row in tempList:
        if row[position] != "s":
            newList += [int(row[position])]
    return newList

totalTests = coloumn(2,tableList)
reading = coloumn(3,tableList)
math = coloumn(4,tableList)
writing = coloumn(5,tableList)

def average(tests,subject):
    newList=[]
    n=0
    for value in subject:
       newList += [subject[n] * tests[n]]
       n += 1
    return sum(newList)/sum(tests)

htmlStats = "<p>Total Number of Tests Taken: " + str(sum(totalTests)) + "<br> Average Number of Tests: " + str(sum(totalTests)/len(totalTests))
htmlStats = htmlStats + "<br> Average SAT Reading Score: " + str(average(totalTests,reading)) + "<br> Average SAT Math Score: " + str(average(totalTests,math))
htmlStats = htmlStats + "<br> Average SAT Writing Score: " + str(average(totalTests,writing)) + "<br> Highest School Average(Stuyvesant's): Reading-" + str(max(reading))+", Math-"
htmlStats = htmlStats + str(max(math)) + ", Writing-" + str(max(writing)) + "</p>"

htmlString = htmlHead + htmlMid + htmlStats + genTable(tableList) + htmlTail

def fileWrite(output,filename):
    outStream = open(str(filename),"w")
    outStream.write(output)
    outStream.close()

fileWrite(htmlString,"statsSAT.html")
