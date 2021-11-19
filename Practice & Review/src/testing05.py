"""
------------------------------------------------------------------------
Adds together 2D lists into one list
------------------------------------------------------------------------
Author:  Chandler Mayberry
Date_last_updated = 2020-01-13
------------------------------------------------------------------------
"""
#imports
from functions import matrixes_add

#2D lists
a = [[0, 1], [2, 3], [4, 5]]
b = [[6, 7], [8, 9], [1, 0]]

#output
c = matrixes_add(a, b)
print(c)