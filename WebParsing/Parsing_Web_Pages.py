#!/usr/bin/python

#!/usr/bin/python

###########################################################
# Script Name:          Parsing_Web_Pages.py
# Creator:              Daniel Svoboda
# Description:          User inputs web page to parse and What to search/parse, Required => First Level indentation, Optional => Second level indentation
# Date of Creation:     2017-12-27
# Last Modification:    2017-12-29
# Modified by:          Daniel Svoboda
# Modified:             added description
# Version:              1.0
# Notes:
###########################################################

# Neccessary packages:
#    1) python3 -m pip install beautifulsoup4
#    2) python3 -m pip install requests

# importing packages/modules
import requests
from bs4 import BeautifulSoup


# FUNCTION => will ask user for url to parse and return it from function
def ask_url():
    url = str(input("\nPlease input the entire url you would like to parse: \n"))
    return url


# FUNCTION => will parse the given url via beautiful soup and return the newly gained string
def parse_with_beautifulsoup(url):
    page = requests.get(url)
    parsed = BeautifulSoup(page.content)
    # prints the output nice-to-read in html format
    # soup = BeautifulSoup([page.content], "html.parser")
    return parsed


# FUNCTION => will search the given parsed text by one or two levels if given and output the result
def find_in_web(parsed_text, first_level_search=None, second_level_search=None):
    while first_level_search is None:
        first_level_search = str.lower(input("\nInput what you want to search in First level indentation: \n"))
    end_result = parsed_text.find_all(first_level_search)
    print(end_result)
    if second_level_search is None:
        go_ahead = str.lower(input("\nDo you want to include search for Second level of indentation? y/n\n"))
        if go_ahead == "y":
            user_input = str(input("\nInput what you want to search in Second level indentation: \n"))
            print(user_input)

    for link in end_result:
        if second_level_search is not None:
            result = link.get(second_level_search)
            print(result)
        else:
            print(link)


if __name__ == '__main__':
    url = ask_url()
    parsed = parse_with_beautifulsoup(url)
    find_in_web(parsed)
    