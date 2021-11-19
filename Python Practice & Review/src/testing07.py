"""
------------------------------------------------------------------------
Rotates a list to the right
------------------------------------------------------------------------
Author:  Chandler Mayberry
Date_last_updated = 2020-01-13
------------------------------------------------------------------------
"""
#imports
from functions import matrix_rotate_right

#list:
''''a = [[6, 7, 3], 
     [8, 9, 1], 
     [1, 0, 1]]'''
    
a = [[1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]]

#output:
b = matrix_rotate_right(a)
#print(a)
print(b)
