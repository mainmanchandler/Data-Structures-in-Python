"""
------------------------------------------------------------------------
calories_by_origin testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
ID:      190688910
Email:   mayb8910@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-21"
------------------------------------------------------------------------
"""

#IF I GO TO USE THIS AGAIN KEEP IN MIND THAT ORIGIN 0/ EMPTY LIST IS AN ERROR AND NEEDS TO BE FIXED

#imports
from Food_utilities import read_foods, calories_by_origin
from Food import Food

food_txt = open('foods.txt', 'r')
food = read_foods(food_txt)

origin = 5 #4
avg_cal_origin = calories_by_origin(food, origin)

print('Avg Calories of food in origin {}: {}cals'.format(Food.ORIGIN[origin], avg_cal_origin))