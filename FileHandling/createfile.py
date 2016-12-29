#!/usr/bin/python

''' 
Creates file
use: 1) >> createfile('/provide/full/destination/path')
	 2) type the name of the file you want to create
	 3) choose file extension you desire (txt, py, sh, ps1)
enjoy!
'''

def createfile(path):
    file = str(input("\nWhat do you wanna call the new file?\n "))
    extension = str(input('''
        What type of file would you want to create:
            a) txt
            b) py
            c) sh
            d) ps1
        '''))
    while True:
        if extension == 'a':
            print("You have chosen .txt")
            break
        elif extension == 'b':
            print("You have chosen .py")
            break
        elif extension == 'c':
            print("You have chosen .sh")
            break
        elif extension == 'd':
            print("You have chosen .ps1")
            break
        else:
            print("You must choose between valid answers!")

    joined = path.__add__(file).__add__(extension)
    newfile = open(joined, 'w')
