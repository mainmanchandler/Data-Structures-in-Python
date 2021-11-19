"""
------------------------------------------------------------------------
Determining if a name is a valid python variable name
------------------------------------------------------------------------
Author:  Chandler Mayberry
Date_last_updated = 2020-01-13
------------------------------------------------------------------------
"""
#imports
from functions import is_valid

#input
var = input('Name checker: ')

#output
valid = is_valid(var)
print('{} : {}'.format(var, valid))



