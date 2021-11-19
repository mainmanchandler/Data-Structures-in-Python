"""
------------------------------------------------------------------------
Food class utility functions1.
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-13"
------------------------------------------------------------------------
"""
from Food import Food
from copy import deepcopy

def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    print("Create a food object by filling in the following:")
    
    name = input('Name: ')
    origin = int(input('Origin\n{}:'.format(Food.origins())))
    vegetarian = input('Vegetarian (Y/N): ')
    calories = int(input('Calories: '))
    
    if vegetarian == 'Y' or vegetarian == 'y':
        vegetarian = True
    else:
        vegetarian = False
    
    food = Food(name, origin, vegetarian, calories)
    
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    seperator = line.split("|")
    food = Food(seperator[0], int(seperator[1]), seperator[2] == "True", int(seperator[3]))

    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    
    foods = []
    
    for loc in file_variable:
        foods.append(read_food(loc))

    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    
    for the_food in foods:
        the_food.write(file_variable)

    return None


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    foods is unchanged.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    
    veggies = []
    
    for the_food in foods:
        if the_food.is_vegetarian == True:
            veggies.append(the_food)

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    foods is unchanged.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    origins = []
    for the_food in foods:
        if the_food.origin == origin:
            origins.append(the_food)
        
    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    total_cal  = 0
    count = 0
    for the_food in foods:
        total_cal += the_food.calories
        count += 1
    
    avg = total_cal // count
    
    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    
    total_cal = 0
    count = 0
    
    for the_food in foods:
        if the_food.origin == origin:
            total_cal += the_food.calories
            count += 1
            
    avg = total_cal // count
    
    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    print( "{:<36}{:<13}{:<11}{}".format( "Food", "Origin", "Vegetarian", "Calories" ) )
    print( "{} {} {} {}".format( '-' * 35, '-' * 12, '-' * 10, '-' * 8 ) )
    
    unchanged_foods = deepcopy(foods)
    unchanged_foods.sort()

    for the_food in unchanged_foods:
        print( "{:<36}{:<13}{:>10}{:>8}".format( the_food.name, Food.ORIGIN[the_food.origin], str(the_food.is_vegetarian), the_food.calories ) )

    return None


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    
    result = []
    for the_food in foods:
        
        if the_food.origin == origin or origin == -1:
            
            if max_cals == 0 or the_food.calories <= max_cals:
                
                if not is_veg or (is_veg and the_food.is_vegetarian):
                    result.append(the_food)
    
    
    return result

