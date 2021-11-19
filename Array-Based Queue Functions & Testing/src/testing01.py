"""
------------------------------------------------------------------------
Testing for Queue_circular class
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-27"
------------------------------------------------------------------------
"""
#imports
from Food_utilities import read_foods
from Queue_circular import Queue


def circular_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Circular Queue are tested for both empty and
    non-empty Circular queues using the data in a:
        is_empty, insert, remove, peek
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    cq = Queue()
    
    print('Empty circular queue: ')
    print('Is_Empty: {}\n\n'.format(cq.is_empty()))    
        
    #fill with values from list "a"
    for i in a:
        cq.insert(i)
        
    print('--The Contents of the Circular Queue:--')
    for i in cq:
        print(i) 
        
    
    print('\nActive circular queue:')
    print('Is_Empty: {}\n\n'.format(cq.is_empty()))
    
    print("--Peek at front of list:-- \n{}\n".format(cq.peek()))
    
    #removal of first in Queue    
    #Verify if the removal and peek for next value
    print('--item removed:-- \n{}\n\n--Next:-- \n{}'.format(cq.remove(), cq.peek()))
    print()
    print('--item removed:-- \n{}\n\n--Next:-- \n{}'.format(cq.remove(), cq.peek()))
    print('\n\n')
    
    print('--Look at behaviour:--')
    for i in cq:
        print(i)
        
    print('\n\n')

    print('--Refilled the circular Queue with [9,0,4] to verify that it chases itself:--')
    #Note that the max size of the array is 10
    b = [9,0,4]
    for i in b:
        cq.insert(i)
        
    for i in cq:
        print(i) 
    
    print('\n\n') 
    print('--item removed:-- \n{}\n\n--Next:-- \n{}'.format(cq.remove(), cq.peek())) #The next one to be removed should be 7
    print('--item removed:-- \n{}\n\n--Next:-- \n{}\n'.format(cq.remove(), cq.peek())) #The next one to be removed should be 7
    print('--item removed:-- \n{}\n\n--Next:-- \n{}\n'.format(cq.remove(), cq.peek())) #The next one to be removed should be 7

    return None



'''
food_txt = open('foods.txt', 'r')
foods = read_foods(food_txt)
circular_queue_test(foods)
'''
a = [2,6,3,7,1]
circular_queue_test(a)

#Note that the current problem with this is that it skips by two when removing and peeking














