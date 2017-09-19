"""
Team <Proper Pronoun>: Connie & Ginevra
IntroCS2 pd8
HW#36 -- Put Your Plan Into Action
2016-04-20

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
"""
import random

def listify(string):
    return string.split(" ")

def replace(List,a,b):
    List[List.index(a)]= b
    return List

def selectRandom(List):
    n = random.randrange(len(List))
    return List[n]

def fillBlanks(story):
    nouns="dog cat hat mat pig pencil".split(" ")
    verbs="walk sat run help smile".split(" ")
    adj="pretty hot cold tall short".split(" ")
    adverbs="gently quite then there".split(" ")
    blanks=["<noun>","<verb>","<adj>","<adverb>"]
    storyList=listify(story)
    for blank in blanks:
        while " ".join(storyList).find(str(p)) > -1:
            replace(storyList,str(p),selectRandom(p))
    finishedStory=" ".join(storyList)
    return finishedStory

storyTest = "Today, a <noun> sat on the <noun> and ran around."
print fillBlanks(storyTest)

# I have a problem where if there is punctuation after the <noun>, the entire thing breaks. Other than that, it works if there
# are multiple blanks, but it is currently limited to only nouns. And it breaks if there is punctuation. So there is that.
    
