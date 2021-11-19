"""
------------------------------------------------------------------------
split_key testing file
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-27"
------------------------------------------------------------------------
"""
#imports
from Priority_Queue_array import Priority_Queue
from utilities import array_to_queue

key = 13
values = [12,25,5,17,10,13,2,33]
#values = [11, 22, 33, 44, 55, 66]
source = Priority_Queue()

#fill the queue up with values
array_to_queue(source, values)

print('--Input Key:--')
print(key)
print('\n--Source:--')
for i in source:
    print(i, end = ' ')
    
#the actual test
target1, target2 = source.split_key(key)

print('\n\nSource is_empty: {}\n'.format(source.is_empty()))

print('\n--Target 1:--')
for i in target1:
    print(i, end = ' ')

print('\n--Target 2:--')
for i in target2:
    print(i, end = ' ')



