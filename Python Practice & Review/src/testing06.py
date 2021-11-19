"""
------------------------------------------------------------------------
Multiplying two 2D lists together 
------------------------------------------------------------------------
Author:  Chandler Mayberry
Date_last_updated = 2020-01-13
------------------------------------------------------------------------
"""
#imports
from functions import matrixes_multiply

#2D Lists
''''a = [[0, 0], 
     [1, 4], 
     [6, 5]]

b = [[6, 7, 3], 
     [3, -1, 1]]
'''
a = [[1,2],[2,1],[2,1],[2,1]]
b = [[1,3,3,4],[1,2,4,5]]

#Outputs
c = matrixes_multiply(a, b)
print(c)
