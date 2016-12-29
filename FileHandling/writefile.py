#!/usr/bin/python

''' 
Write into file
use: 1) >> writefile('/provide/full/path/to/file')
	 2) type what you would like to input into the file
	 
enjoy!
'''

def writefile(path):
    with open(path, 'a') as f:
        i = str(input("\nWhat you wanna put in the file?\n "))
        f.write(i)
