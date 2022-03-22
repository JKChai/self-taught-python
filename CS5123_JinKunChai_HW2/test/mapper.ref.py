# -*- coding: utf-8 -*-
"""mapper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YqnG_JgNng7CJBBnYD97ziRzA_Os4ITV
"""

#!/usr/bin/python3
"""mapper.py"""
import os
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # line is a line from the file input. EXAMPLE line: I love Oklahoma
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the Reduce step, the input for reducer.py
        # tab-delimited; the trivial word count is 1
        print('%s\t%s' % (word, 1))
        # NOTE: Mapper output is intermediate and it is written to the disk (HDFS)
        # EXAMPLE OUTPUT:
        #(I  1)
        #(love  1)
        #(Oklahoma  1)