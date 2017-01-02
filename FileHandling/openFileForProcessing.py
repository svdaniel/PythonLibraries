#!/usr/bin/python3

def openFileForProcessing(path):
    '''
    Opens file + parses it via BeautifulSoup and returns the json output for further processing
    returns type => <class 'bs4.BeautifulSoup'>
    '''
    from bs4 import BeautifulSoup
    with open(path) as f:
        soup = BeautifulSoup(f)
    return soup
    