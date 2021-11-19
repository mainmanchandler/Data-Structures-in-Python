"""
------------------------------------------------------------------------
 Finding the smallest, largest, total and average values in a 2D list
------------------------------------------------------------------------
Author:  Chandler Mayberry
Date_last_updated = 2020-01-13
------------------------------------------------------------------------
"""
#imports
from functions import matrix_stats

#2D list:
a = [[1,2],[2,2],[-5,7],[3,-1],[0,0]]

#output
small, large, total, average = matrix_stats(a)
#print(a)
print('{},{},{},{}'.format(small, large, total, average))