#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
import random

def selectRandom(List):
    n = random.randrange(len(List)) 
    return List[n] 

def correspond(blankType):
    noun = "dog cat hat mat mother apple sweator laptop book food chair toy pen arm coat corn cow wind \
window wood top toy rain rin picture pig money milk garden grass egg".split(" ")
    noun_plural = "boats houses rivers cats buses wishes pictures boxes pennies spies daisies flowers foci cacti eleves lives mice geese".split(" ")
    verb = "walk sit run cry awake be beat begin band bend bring come do draw find forgive get give go have hear rise run say stand swim \
tear tell think throw understand hurt keep lead grow hand hang".split(" ")
    verb_past = "ran sat awoke did drew drove fell forgave froze got gave rose slept spent spoke rand read lost made meant".split(" ")
    adverb = "quietly silently easily warmly quickly mainly freely often unfortunately.".split(" ")
    adjective = "shiny cheap well-made tiny large huge young old antique teenaged tall hot cold long short frail \
aggressive agile agitated agonizing agreeable ajar alarmed alarming alert alienated alive all altruistic bogus \
boiling bold bony boring bossy both bouncy bountiful bowed".split(" ")
    location = ["New York","home","Los Angeles","California","Las Vegas","Grand Canyon","San Fransico","Housten","Chicago","San Jose"]
    weather = "humid wet dry foggy windy freezing cold hail rain sleet cloudy sunny clear".split(" ")
    food = "burgers french-fries corn pasta potatoes strawberries yogurt butter bagels donuts coffee chicken salads".split(" ")
    number = "one two three thirty-four fourty-two four-hundred-twenty eighty-one nine-hundred-ninety-nine twenty-three seventy-eight fifty-six thirty-three".split(" ")
    celebrities = ["Lauren Conrad","Joan Rivers","Rumer Willis","Hilary Duff","Heather Locklear","Liv Tyler","Lucy Liu","Gerald Butler","Halle Berry"]
    color = "blue red orange yellow magenta violet indigo green gray black white".split(" ")
    blanks = ["<noun>","<noun (plural)>","<verb>","<verb (past)>","<adverb>","<adjective>","<location>","<weather>","<food>","<number>","<celeb name>","<color>"]
    blankL = [noun,noun_plural,verb,verb_past,adverb,adjective,location,weather,food,number,celebrities,color]
    if blankType == "base":
        return blanks
    else:
        return blankL[blanks.index(blankType)]

def capsCheck(story,punctuation):
    unchecked = story 
    checked = ""
    while len(unchecked) > 0 and unchecked.find(punctuation) > -1 and unchecked.find(punctuation) != len(unchecked) -1:
        checked = checked + unchecked[:unchecked.find(punctuation)+2] + unchecked[unchecked.find(punctuation)+2].capitalize()
        unchecked = unchecked[unchecked.find(punctuation)+3:]
    return checked + unchecked

def fillBlanks(story):
    blanks = correspond("base")
    for blankType in blanks:
        while story.find(blankType) != -1:
            story = story.replace(blankType, selectRandom(correspond(blankType)), 1)
    punctuation = [".","!","?"]
    while len(punctuation) > 0:
        story = capsCheck(story,punctuation[0])
        punctuation[:1] = []
    return story

def madlibify():
    story1 = "Albert Einstein, the son of <b><celeb name></b> and <b><celeb name></b>, \
was born in <b><location></b>, Germany, in 1879. In 1902, he had a job \
as assistant <b><noun></b> in the Swiss patent office and attended \
the University of Zurich. There he began studying atoms, molecules, \
and <b><noun (plural)></b>. He developed the theory of \
<b><adjective></b> relativity, which expanded the phenomena of sub-atomic \
<b><noun (plural)></b> and <b><adjective></b> magnetism. In 1921, \
he won the Nobel prize for <b><noun (plural)></b> and was director of \
theoretical physics at the Kaiser Wilhelm <b><noun></b> in <b><location></b>. \
In 1933, when <b><celeb name></b> became Chancellor of <b><location></b>, \
Einstein came to <b><location></b> to take a post at Princeton Institute for \
<b><noun (plural)></b>, where his theories helped America devise the first \
atomic <b><noun></b>. There is no question about it: Einstein was \
one of the most brilliant <b><noun></b> of our time."
    story2 = "Elizabeth, the Tudor <b><noun></b> of <b><location></b>, was probably the \
<b><adjective></b> ruler the British ever had. Elizabeth was the \
daughter of Henry the <b><number></b> and Anne Boleyn. Later, Anne had \
her <b><noun></b> chopped off by Henry. \
Elizabeth was born in 1533 and became queen when she was <b><number></b>. She \
was a(n) <b><adjective></b> Protestant and persecuted the <b><adjective></b> \
Catholics <b><adverb></b>. In 1588, the Armada attacked England. But the English fleet, commanded by <b><celeb name></b> \
and <b><celeb name></b>, defeated them. Elizabeth ruled for <b><number></b> years, \
and during her reign England prospered and produced Shakespeare, \
Francis Bacon, and <b><celeb name></b>. Elizabeth never married, \
which is why she is sometimes called the <b><adjective></b> Queen."
    story3 = "A Link Trainer is a(n) <b><adjective></b> airplane that never leaves the \
<b><noun></b>. It is used to teach beginning <b><noun (plural)></b> the \
principles of flying. It has a(n) <b><noun></b>, and a full set of \
<b><noun (plural)></b>, just like a regular airplane. It can imitate any \
sort of aerial manuever such as loop-the-<b><noun></b> or \
a(n) <b><adjective></b> dive, and it is very safe. Nothing can happen to you \
unless, of course, you forget to fasten your safety <b><noun></b>. \
Then you might fall out on your <b><noun></b>. \
After a student passes the tests on the Link Trainer, he then gets into \
a real plane and learns to taxi down the <b><noun></b>. And he \
learns to tell which way the <b><noun></b> is blowing before he \
takes off into the 'Wild <b><color></b>. Yonder!' Then, in no time, \
he learns to take off and is flying <b><number></b> miles per hour at a \
height of <b><number></b> feet. When he does this, he is a real pilot."
    print fillBlanks(selectRandom([story1,story2,story3]))

madlibify()

