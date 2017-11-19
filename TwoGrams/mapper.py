#!/usr/bin/env python

import re
import sys
import string
# input comes from STDIN (standard input)

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    line = re.sub(r'[^0-9a-zA-Z]+',' ',line).split()

    #Convert all the words into lower case
    line = list(map(lambda x: x.lower(), line))
    words = []
    for i in range(len(line)):
        try:
            words.append(line[i]+" "+line[i+1])
        except:
            words.append(line[i])
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word, 1)