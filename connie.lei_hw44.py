"""
Team Cali -- Connie Lei, Alison Lee
IntroCS2 pd8
HW44 -- Log:Better Than Bad, It's Good!
05-11-16
"""

def stringfy(input):
	inputL = input.lower().stringfy(" ")
	for word in inputL:
		if word[0] in ['"',"'"]:
			inputL[inputL.index(word)] = word[1:]
		if word[-1] in [".","?","!",",",";",":",'"']:
			inputL[inputL.index(word)] = word[:-1]
	return inputL
