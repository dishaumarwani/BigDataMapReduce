#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
import numpy

#number of columns of A/rows of B
n = int(sys.argv[1])

#Create data structures to hold the current row/column values (if needed; your code goes here)


array = list()
currentkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

	#Remove leading and trailing whitespace
	line = line.strip()
	inp = "{\t}''"
	out = '     '
	transtab = str.maketrans(inp, out)
	line = line.translate(transtab)
	#Get key/value
	key, value = line.split(':',1)

	#Parse key/value input (your code goes here)
	key = key.strip()
	values = value.strip().split(" ")
	value = values[2]

	#If we are still on the same key...
	if key==currentkey:

		#Process key/value pair (your code goes here)
		array.append(value)
		array = list(map(float, array))


	#Otherwise, if this is a new key...
	else:
		#If this is a new key and not the first key we've seen
		if currentkey:
			alist = array[:int(len(array)/2)]
			blist = array[int(len(array)/2):]
			currentsum = sum([x*y for x,y in zip(alist, blist)])
			print('%s\t%s' % (currentkey, currentsum))

		currentkey = key

		#Process input for new key (your code goes here)


		array = []
		array.append(value)
		array = list(map(float, array))

#Compute/output result for the last key (your code goes here)

alist = array[:int(len(array)/2)]
blist = array[int(len(array)/2):]

currentsum = sum([x*y for x,y in zip(alist, blist)])

print('%s\t%s' % (currentkey, currentsum))
