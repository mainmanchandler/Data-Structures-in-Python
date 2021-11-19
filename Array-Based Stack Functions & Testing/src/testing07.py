"""
------------------------------------------------------------------------
stack_maze in functions testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-26"
------------------------------------------------------------------------
"""
#imports
from functions import stack_maze


maze = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'], 'D':[], 'E':['F', 'X'], 'F':['G', 'H'], 'G':[], 'H':[]}

maze1 = {'Start': ['X']}

maze2 = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'], 'D':[], 'E': ['X', 'F'], 'F':['G'], 'G':['C']} #with circular path

maze2_ver2 = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'], 'D':[], 'E': ['F', 'X'], 'F':['G'], 'G':['C']} #with circular path

maze3 = {'Start': ['A'], 'A':[]} #with no exit

maze4 = { 'Start': ['B', 'A'], 'A':['C','D'], 'B':['X'], 'C':[], 'D':[] }

path = stack_maze(maze2_ver2)
print("Path taken: {}".format(path))




