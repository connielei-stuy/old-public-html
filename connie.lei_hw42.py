"""
Team Cyan -- Connie Lei, Ryan Siu
IntroCS2 pd8
HW42 -- Four de Toid Thyme
2016-05-08

1. modeLB(nums) returns the mode of the set of numeric elements in list nums.
Uses a dictionary to implement the "labeled buckets" algorithm.
modeLB( [0,5,7,3,2,3] ) = 3
modeLB( [0,5,7,3,7,3] ) = 3  ( or 7 )
"""

def modeLB(nums):
    counter = dict()
    for number in nums:
        if number in counter:
            counter[number] = counter[number] + 1
        if number not in counter:
            counter[number] = 1
    largest = nums[0]
    for number in counter:
        if counter[number] > counter[largest]:
            largest = number
    final = str(largest)
    for number in counter:
        if counter[largest] == counter[number] and largest != number:
            final += " or "
            final += str(number)
    return final
	
modeLB([0,5,7,3,2,3])
modeLB([0,5,7,2,7,3])
