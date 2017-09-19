#!/usr/bin/python
print "content-type: text/html\n"
print ""

"""
Team Cali - Connie Lei, Alison Lee
IntroCS2 pd8
HW46 -- Maxim:Don't timeout and don't get sued.
2016-05-11
"""

lit = open( "lit.txt" , "r" )
text = lit.read()
lit.close()

def stringfy(txt):
    tally = { }
    inputL = txt[662:563017]
    inputL = txt.lower()
    inputL = inputL.split()
    return len(inputL)

length = stringfy(text)

# this function is primarily for the % calculations

blacklist = "the us most day give the be too of and a in that have i it for not on with he as \
 you do at this but his by from they we say her she or an will my one all would there their what so \
up out if about who get which go me when make can like time no just yes know take people into see \
other look only also think most first even want use after is were must could man him upon am shall \
had to said your our some over very should may am upon ".split() + ['back','down','are','any','before','two','been','how','much','has','was','more','then','the\
m','here','now','come','than','might','well','matter','where','came']

def stringfyTheTally(txt):
    tally = { }
    inputL = txt[662:563017]
    inputL = txt.lower()
    inputL = inputL.split()
    for word in inputL:
        newW = word.strip('".?,:!;\n')
        if ( not newW in blacklist ) and ( newW in tally ) :
            tally[ newW ] += 1
        elif not word in blacklist :
            tally[ newW ] = 1
    return tally

# this was just to decrease the run time so instead of making two loops, one to update all the punctuation and the other to count and place into the correct
# dictionary, this was combined into two functions

tally = stringfyTheTally( text )

def topn( d , n ) :
    finalDN = { }
    key = d.keys()
    value = d.values()
    newKey = []
    newValue = []
    while n > 0 :
        tempV = value.index( max( value ))
        newValue += [max( value )]
        newKey += [key[tempV]]
        del value[ tempV ]
        del key[ tempV ]
        n -= 1
    return [newKey,newValue]

# this takes out the top 30 values and puts them into sorted lists, combined function to decrease run time
   
def tablefy( d ):
    print "<table border = '1' align='center'> \n<r> <td colspan='3'> Top 30 Most Common Words </td></r> \n<tr> \
<td> Word </td> <td> Frequency </td> <td> Percentage </td></tr>"
    keys = d[0]
    values = d[1] # this allows us to choose the two list inputs and seperate them
    for i in keys :
        iPos = keys.index(i)
        print "<tr> <td> " + str( i ) + " </td> <td> " + str( values[iPos] ) \
              + " </td> <td> " + str( float( values[iPos] ) / length * 100 ) + "% </td> </tr>" 
    print "</table>"

print '<!DOCTYPE html> \n<html> \n<body style="text-align:center">'
print "<h2><b> The Adventures of Sherlock Holmes </b></h2>\n"
print "<h4>by <i>Arthur Conan Doyle</i><h4>\n"
print '<a href="lit.txt">Full Story</a>'
print "<h2> Blacklist of Common Words</h2> \n<p>" + (" ").join(blacklist) + "</p>"
print "<p> This is a function that finds the top thirty most used words, excluding those mentioned in the blacklist. I divided the story into different words, including\
punctuation. Then I strip the word of the punctuation and create a dictionary counter. I do not update the words in order to lower runtime. After the dictionary\
 is created, the top thirty words are seperated out into two lists. Those lists are run through a for loop and changed into html format. <p>"

htmlInput = topn(tally,30)
tablefy(htmlInput)

print '</body> \n</html>'

