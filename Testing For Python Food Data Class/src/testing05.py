"""
------------------------------------------------------------------------
food_search testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
ID:      190688910
Email:   mayb8910@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-21"
------------------------------------------------------------------------
"""
#imports
from Food_utilities import read_foods, food_search, food_table
from Food import Food

food_txt = open('foods.txt', 'r')
food = read_foods(food_txt)

origin = int(input('Enter food origin from list:\n{}'.format(Food.origins())))
max_cals = int(input('Enter the desired max amount of calories for the food: '))

is_vege = input('Vegetarian? Type(Y/N): ')
if is_vege == 'y' or is_vege == 'Y':
    is_veg = True
else:
    is_veg = False
    
food_criteria = food_search(food, origin, max_cals, is_veg)

print('Food that matches your personalized criteria: \n')
food_table(food_criteria)

