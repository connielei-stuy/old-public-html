#!/usr/bin/python

yellow=[[4,1],[12,1],[15,4],[1,4],[4,15],[12,15],[1,12],[15,12]]
blue=[[2,3],[2,13],[3,2],[3,5],[3,14],[3,11],[5,3],[5,7],[5,9],[5,13],[7,5],[7,11],\
      [14,3],[14,13],[13,2],[13,5],[13,14],[13,11],[11,3],[11,7],[11,9],[11,13],[9,5],[9,11]]
red = [[2,6],[2,10],[4,8],[6,2],[6,14],[8,4],[8,12],[10,14],[10,2],[14,6],[14,10],[12,8]]
green=[[1,7],[1,9],[4,4],[4,12],[6,6],[6,10],[7,1],[7,15],[9,1],[9,15],[10,6],[10,10],[15,7],[15,9],[12,4],[12,12]]
colors = yellow + blue + red + green + [[8,8]]

def colorize(n,r):
    start = "\t\t<td width='50px' height='50px'"
    ending = "'size='1'maxlength='1'>\n\t\t</td>\n"
    if [n,r] in colors:
        cords=[n,r]
        if cords in yellow:
            return start + "bgcolor='yellow'>\n\t\t\t<input type ='text' name='" + str(n) + "," + str(r)+ ending
        if cords in red:
            return start + "bgcolor='red'>\n\t\t\t<input type ='text' name='" + str(n) + "," + str(r)+ ending
        if cords in green:
            return start + "bgcolor='green'>\n\t\t\t<input type ='text' name='" + str(n) + "," + str(r)+ ending
        if cords == [8,8]:
            return start + "bgcolor='purple'>\n\t\t\t<input type ='text' name='" + str(n) + "," + str(r)+ ending
        if cords in blue:
            return start + "bgcolor='blue'>\n\t\t\t<input type ='text' name='" + str(n) + "," + str(r)+ ending
    else:
        return start + ">\n\t\t\t<input type ='text' name='" + str(n) + "," + str(r)+ ending

def table():
        html = "<html>\n <form name = 'input' method ='POST' action ='updateWord.py'>\n\
<table border='1'align='center'>\n"
        r = 1
        while r < 16:
                tableRow = "\t<tr>\n"
                n = 1
                while n != 16:
                        tableRow += colorize(n,r)
                        n += 1
                r += 1
                tableRow += "\t</tr>\n"
                html += tableRow
        html += "</table>\n</html>"
        return html

htmlString = table()

def fileWrite(output,filename):
    outStream = open(str(filename),"w")
    outStream.write(output)
    outStream.close()

fileWrite(htmlString,"table.html")
