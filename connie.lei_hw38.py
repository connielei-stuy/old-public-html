"""
Team <Proper Pronoun>: Connie & Ginevra
IntroCS2 pd8
HW#38 -- Tunr Your Engine
2016-04-30

Mechanism for Madlibification
1. Have several lists for each group of words, basically have a VERBS, NOUNS, PRONOUNS, ADVERBS, etc. list.
2. Have the background/layout format prewritten, so if we have a long paragraph, we will have a skeleton and 
   then have random selections from the lists depending on what needs to be filled into the blank.
3. Have another function that selects a random value from the list. This will be done like str(random.VERBS)
   or something.
4. Perhaps have another function that will also remove that value so that we don't have continuous reuse of 
   the same words.
5. We have to ensure that the list of each category is longer than the number needed or else we will have to
   repeat some words. But this should be last resort.
6. Another idea is that we can have the skeleton saved as a string and instead of building a skeleton, we could
   have a function that would allow other skeletons to be inputted. (not sure how this will work)

New Features in Version 2:
1. Pronunciation works.
2. Increased amounts of specific nouns or verbs
3. Grammar works
4. Capitalization
"""
##import random
##
##def listify(string):
##    return string.split(" ")
##
##def replace(List,a,b):
##    List[List.index(a)]= b
##    return List
##
##def selectRandom(List):
##    n = random.randrange(len(List)-1)
##    return List[n]
##
##def fillBlanks(story):
##    nouns="dog cat hat mat".split(" ")
##    storyList=listify(story)
##    while " ".join(storyList).find("<noun>") > -1:
##        replace(storyList,"<noun>",selectRandom(nouns))
##    finishedStory=" ".join(storyList)
##    return finishedStory
##
##storyTest = "Today, a <noun> sat on the <noun> and ran around."
##print fillBlanks(storyTest)

import random

def selectRandom(List):
    n = random.randrange(len(List)) # since randrange is exclusive for the number, we don't need to subtract one
    return List[n] # this should return a string

def correspond(blankType):
    noun = "dog cat hat mat".split(" ")
    verb = "walk sit run cry jump fall yell apologize announce ask assert awake dive divide empty encode enchant emigrate".split(" ")
    verb-past = "ran read cried sat fell".split(" ")
    adverb = "quietly silently".split(" ")
    adjective = ["pretty","large","hot","cold","sad","tall"]
    location = ["New York","home"] # this is an example of when you can't used the .split(" ") so instead you have to manually type it our
    blanks = "<noun> <verb> <adverb> <adj> <location>".split(" ")
    blankL = [noun,verb,adverb, adjective,location]
    if blankType == "base":
        return blanks
    else:
        return blankL[blanks.index(blankType)]

# correspond acts as our memory and holds everything that we need to know, basically this is the function where you can add
# all the different blank types that you want. If you want to have a word with a space in between, you'll need to write the
# replacement options in the a list format instead of just typing them in a string. You'll also have to add the corresponding
# <replacement> and the replacement string in the same position in two different lists. (Actually I could change that so that a single
# list holds two lists! Actually, that is so smart but that'll start to get confusing so I won't change anything right now. Maybe in
# a different version.) Another thing is that you'll also have to update the blanks list in the fillBlanks function so that it equals the
# on in the correspond function. (Actually I changed it so you don't have to.) If you wanted to add the grammar, you would simply create a new
# lsit that is called verb-past-tense and then have the story have <verb-past-tense> or <verb past tense>.


"""def capsCheck(story,puncuation):
    unchecked = story
    checked = ""
    while len(unchecked) != 0 unchecked.find(puncuation):
        unchecked = [unchecked.find(puncuation)+2:]
        checked = checked + unchecked[unchecked.find(puncuation)+1:] + unchecked[unchecked.find(puncuation)].capitalize()
    return checked + unchecked"""

def fillBlanks(story):
    blanks = correspond("base")
    for blankType in blanks:
        while story.find(blankType) != -1:
            story = story.replace(blankType, selectRandom(correspond(blankType)), 1)
            print story
    """puncuation = [".",'"',"!","?"]
    for eachType in puncuation:
        story = capsCheck(story,puncuation)"""
    return story

print fillBlanks("I <verb> by the <noun> and <noun> and <verb> that the <noun> has <verb>.")
 #print fillBlanks("Three Little Pigs /n by: <your name> /n Once upon a time, there were three <adj> pigs. One day, their mother said, 'You are all \
# grown up and must <verb> on your own.' So they left /n to <verb> their houses. The first little pig wanted only to <verb> all day and <adverb> built \
# his house out of <noun-plural>. The second little pig wanted to <verb> and <verb> all day so he <verb-past> his house with <noun-plural>. The third \
# <adj> pig knew the wolf lived nearby and worked hard to <verb> his house out of <noun-plural>. One day, the wolf knocked on the firt pig's <noun>. 'Let me in in or I'll\
# or I'll <verb> your house down!'")
