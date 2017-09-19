# Team -- Connie Lei, Derek Chen, Iris Tao
# IntroCS2 pd8
# HW15 -- Loopy
# 2016-03-14

# 1. sumDigits(n) takes a positive integer n and returns the sum of its digits.

def sumDigits (n):
    a = 0
    while n > 0:
        a = a + n % 10
        n = n / 10
    return a

# sumDigits(0) should be 0
# sumDigits(1) should be 1
# sumDigits(12) should be 3
# sumDigits(1112) should be 5

print sumDigits(0), sumDigits(1),sumDigits(5), sumDigits(12), sumDigits(1112)

# 2. squares(n) takes a positive integer n and prints each integer from 1 to n,
# inclusive, along with its square. The number and its square should appear on
# the same line.

def squares(n):
    while n > 1:
        print n , n ** 2
        n = n - 1
    print n ,n
    
# squares(5) should be
# 5, 25
# 4, 16
# 3, 9
# 2, 4
# 1, 1

squares(5)

# I keep getting None and I can't figure out why!!!

# 3. sumPerfSqs(n) takes a positive integer n and returns the sum of the perfect
# squares between 1 and n, inclusive.

def sumPerfSqs(n):
    a = 0
    while n > 0:
        a = a + n ** 2
        n = n-1
    return a

# sumPerfSqs(5) should be 55

print sumPerfSqs(5)
