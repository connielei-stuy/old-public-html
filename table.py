def table():
	html = "<html>\n <table border='1'align='center' >"
	r = 1
	while r != 16:
		tableRow = "\t<tr>\n"
		r += 1		
		n = 1
		while n != 16:
			tableRow += "\t\t<td width='50px' height='50px'></td>\n"
			n += 1
		tableRow += "\t</tr>\n"
		html += tableRow
	html += "</table>\n</html>"
	return html

def cellData():
	

htmlString = table()

def fileWrite(output,filename):
    outStream = open(str(filename),"w")
    outStream.write(output)
    outStream.close()

fileWrite(htmlString,"table.html")
