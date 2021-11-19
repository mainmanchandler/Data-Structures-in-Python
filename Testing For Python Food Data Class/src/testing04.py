"""
------------------------------------------------------------------------
food_table testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
ID:      190688910
Email:   mayb8910@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-21"
------------------------------------------------------------------------
"""
#imports
from Food_utilities import food_table, read_foods

food_txt = open('foods.txt', 'r')
food = read_foods(food_txt)

food_table(food)

