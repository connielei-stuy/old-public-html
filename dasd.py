def word(number):
    wordL=["zero","one","two","three","four","five","six","seven","eight","nine"]
    return wordL[number]

def engSpan(word):
    spanish=["por favor","gracías", "si","no","salud"]
    english=["please","thank you","yes","no","bless you"]
    if word in english:
        return spanish[english.index(word)]
    if word in spanish:
        return english[spanish.index(word)]
    return None
