"""
------------------------------------------------------------------------
Determines various amounts of characters in a file
------------------------------------------------------------------------
Author:  Chandler Mayberry
Date_last_updated = 2020-01-13
------------------------------------------------------------------------
"""
#imports
from functions import file_analyze

#open file
file = open('t08.txt','r')

#output
u, l, d, w, r = file_analyze(file)
print('{}, {}, {}, {}, {}'.format(u,l,d,w,r))

