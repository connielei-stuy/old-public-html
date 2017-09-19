"""
Connie Lei
IntroCS2 pd9
HW26--Float Like a Butterfly, Sting Like a Bee
2016-04-04

1.minPos(L) takes a list L containing only numeric elements,
and returns the position (index) of the least value.
"""

def minPos(L):
    small=0
    position = 0
    while len(L) > position:
        if L[position] >= L[small]:
            position += 1
        else:
            small = position
    return small

print minPos( [3] ) # → 0
print minPos( [5,4,3,2,1] ) # → 4
