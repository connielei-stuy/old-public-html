"""
Connie Lei
IntroCS2 pd8
HW#28-- For vs. While
2016-04-10

 WvF: <I don't understand how for works so I just used while. Google doesn't help.>

 1. rmNegatives(L) removes the negative numbers from list L, assumed to contain only numeric elements. (Modifies L; does not create a new list.)
rmNegatives( [5,4,3,2,1] ) → [5,4,3,2,1]
rmNegatives( [5,-4,3,-2,1] ) → [5,3,1]
2. listFib(n) returns a list of the first n Fibonacci numbers, starting with 0 as the 0th term, 1 as the 1st term, 1 as the 2nd term, and so on.
listFib(1) → [0]
listFib(2) → [0,1]
listFib(3) → [0,1,1]
listFib(4) → [0,1,1,2]
3. sentify(L) returns a string comprised of list L’s elements, in order, with spaces between. Assumes L contains only string elements.
sentify( [“this”, “is”, “how”, “we”, “do”] ) → “this is how we do”
"""

def rmNegatives(L):
	n=0
	while n < len(L):
		if L[n] < 0:
			L= L[:n] + L[n+1:]
			n -= 1
		n += 1

def listFib(n):
	L=[0,1,1,2]
	if n < = 4:
		return L[:n-1]
	n-4
	while n >0:
		L.append(L[-1]+L[-2])
		n -=1
	return L

def sentify(L):
	s=""
	while L != []:
		s += L[0]
	return s
		