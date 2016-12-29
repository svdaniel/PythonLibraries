#!/usr/bin/python

''' 
Reads given file
use: 1) >> readfile('/provide/full/path/to/file')

enjoy!
'''

def readfile(path):
    with open(path) as f:
        for line in f:
            print(line, end='')
