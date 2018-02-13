
import sys
import string
import numpy

#number of rows in A
m = int(sys.argv[1])

#number of columns in B
p = int(sys.argv[2])


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

	#Remove leading and trailing whitespace
	line = line.strip()

	#Split line into array of entry data
	entry = line.split(",")

	# Set row, column, and value for this entry
	row = int(entry[1])
	col = int(entry[2])
	value = float(entry[3])

	#If this is an entry in matrix A...
	if (entry[0] == "A"):

		#Generate the necessary key-value pairs
 		#(your code goes here)
		for a in range(0,p):
			data = dict()
			data[str(row) + str(a)] = "A " +  str(col)+ " " + str(value)
			print(data)


	#Otherwise, if this is an entry in matrix B...
	else:

		#Generate the necessary key-value pairs
 		#(your code goes here)
		for a in range(0,m):
			data = dict()
			data[str(a) + str(col)] = "B " +  str(row) + " " + str(value)
			print(data)

