# Connie Lei
# IntroCS2 pd8
# HW20 -- Reaching out to neighbors
# 2016-03-23

# 1. closerNum(target,num1,num2) operates on 3 numeric parameters, returning
# a string stating which of the 2nd and 3rd arguments is closer to the first.

def closerNum(target,num1,num2):
    if abs(target-num1) > abs(target-num2):
        return str(target) + " is closer to " + str(num2) # when the distance is larger, then it reports the other
    elif abs(target-num2 )> abs(target-num1):
        return str(target) + " is closer to " + str(num1) # when the distance is larger, then it reports the other
    else:
        return str(target) + " is equally close to " + str(num1)+ " and " + str(num2)

print closerNum(8,20,10) # → “8 is closer to 10”
print closerNum(8,20,2) # → “8 is closer to 2”
print closerNum(8,-2,30) # → “8 is closer to -2”
