# Connie Lei
# IntroCS2 pd 8
# HW17 -- 000 000 111
# 2016-03-17

# 1. bondify(name) takes a name written in First Last format, and returns the sassy version, as shown below.
# bondify(“James Bond”) → “Bond, James Bond”

s="James Bond"

print s.index (" ")
print len(s)

def bondify(n):
	string= n[n.index(" "):len(n)] # *
	string += ", "                 # **
	string += n					   # ***						
	return string				   # ****

# *this creates the last name by identfying where the beginning of the last name starts, then finds the length 
# of the string and therefore the last number, creating a set of the vaues that are the last name

# **this adds the next part, after the last name, it could have been combined but this way is more user friendly

# ***this adds the repeated name

# ****this returns the combined string 
	
print bondify("James Bond")