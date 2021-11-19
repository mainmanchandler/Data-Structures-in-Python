"""
------------------------------------------------------------------------
split_alt testing file
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-27"
------------------------------------------------------------------------
"""
#imports
from Priority_Queue_array import Priority_Queue
from utilities import array_to_queue


values = [10,25,15,20,35,45,30]
#values = [66, 55, 44, 33, 22, 11]
source = Priority_Queue()

#fill the queue up with values
array_to_queue(source, values)

print('--Source:--')
for i in source:
    print(i, end = ' ')
    
#the actual test
target1, target2 = source.split_alt()

print('\n\nSource is_empty: {}'.format(source.is_empty()))

print('\n--Target 1:--')
for i in target1:
    print(i, end = ' ')

print('\n--Target 2:--')
for i in target2:
    print(i, end = ' ')


