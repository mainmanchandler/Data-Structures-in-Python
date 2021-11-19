"""
------------------------------------------------------------------------
Turns a 2D list into a 1D list 
------------------------------------------------------------------------
Author:  Chandler Mayberry
Date_last_updated = 2020-01-13
------------------------------------------------------------------------
"""
#imports
from functions import matrix_flatten

#2D Lists
a = [[1,2],[2,2,7,8],[-5,7],[3,-1],[0,0]]
#a = [['a', 'b'], ['x', 'z'], ['e', 'f']]


#output
b = matrix_flatten(a)
#print(a)
print(b)