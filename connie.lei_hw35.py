"""
Team <Proper Pronoun>: Connie & Ginevra
IntroCS2 pd8
HW#35 -- Best laid plans...
2016-04-19

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