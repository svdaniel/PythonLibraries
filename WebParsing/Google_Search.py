#!/usr/bin/python

'''
###########################################################
# Script Name:          Google_Search.py
# Creator:              Daniel Svoboda
# Description:          user inputs what & how much output google should return + stripped down only to return web links
# Date of Creation:     2017-12-27
# Last Modification:    2017-12-29
# Modified by:          Daniel Svoboda
# Modified:             added description
# Version:              1.0
# Notes:                
###########################################################
'''

# Import Packages
import requests
from bs4 import BeautifulSoup
import re


def get_google_links(search_value=None, return_lines=10):
    # If no arguments are given, gather them
    while search_value is None:
        search_value = str(input("\nPlease specify what you wanna search on google: \n"))
    if return_lines is 10:
        verify = str.lower(input("\nWould you like to change number of values returned? (Default is 10) y/n \n"))
        if "y" in verify:
            return_lines = input("\nHow many values would you like to return: \n")

    # Replace any White_Space in given search value with "%20"
    what_to_search = search_value.replace(' ', '%20')

    # Complete the Search Query
    query = "https://www.google.cz/search?num=" + str(return_lines) + "&q=" + what_to_search

    # Read and save the Result of the Query in local variable
    result_of_query = requests.get(query)

    # Use BeatifulSoup to make the output more readable
    soup = BeautifulSoup(result_of_query.content, "html.parser")

    # Search for output that match "a" pattern
    links = soup.find_all("a")
    for link in links:
        # From output that matches "a" pattern, take only those that further match "href" and also "http"
        if "http" in link.get("href"):
            # regex: may include "http" or "https" or "www" then any charset until "." and then
            # any charset of 0-3 (cz,com...) and all the rest of the link behind
            # regex = r"[htps]{0,3}[w]{0,3}.*\.[a-z]{1,3}.*"
            regex = r"[htps]{0,5}\:*\/*[w]{0,3}\w*\.[a-z]{1,3}[\w\/_%?=&:-]*"

            # Compile regex to be usable
            pattern = re.compile(regex)

            # Use the regex.findall method to parse whats left from links that matched the "href"
            complete = re.findall(pattern, str(link.get("href")))
            print(complete)
            return complete


if __name__ == '__main__':
    get_google_links()
