"""
------------------------------------------------------------------------
Takes out all characters that are not vowels in a string
------------------------------------------------------------------------
Author:  Chandler Mayberry
Date_last_updated = 2020-01-13
------------------------------------------------------------------------
"""
#imports
from functions import dsmvwl

#input
s = 'I think your book is an utter piece of Garbage.'

#output
new = dsmvwl(s)
print('sentence: {}'.format(s))
print('disemvowelled: {}'.format(new))