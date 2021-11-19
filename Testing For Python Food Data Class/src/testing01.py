"""
------------------------------------------------------------------------
by_origins testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
ID:      190688910
Email:   mayb8910@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-21"
------------------------------------------------------------------------
"""
#imports
from Food import Food
from Food_utilities import by_origin, read_foods


food_txt = open('foods.txt', 'r')
food = read_foods(food_txt)

#which category of food
origin = 5
origin_category = by_origin(food, origin)

print('Food Origin: {}\n'.format(Food.ORIGIN[origin]))
for the_food in origin_category:
    print(the_food,'\n')
