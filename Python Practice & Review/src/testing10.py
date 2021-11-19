"""
------------------------------------------------------------------------
Converts words to Pig Latin
------------------------------------------------------------------------
Author:  Chandler Mayberry
Date_last_updated = 2020-01-13
------------------------------------------------------------------------
"""
#imports
from functions import pig_latin

#input
word = input('Enter word: ')

#output
pl = pig_latin(word)
print(pl)