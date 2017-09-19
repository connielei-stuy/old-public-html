def rmNegatives(L):
	n=0
	while n < len(L):
		if L[n] < 0:
			L= L[:n] + L[n+1:]
			n -= 1
		n += 1
