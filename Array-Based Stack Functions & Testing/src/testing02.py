"""
------------------------------------------------------------------------
Split_alt testing from Stack_array Class
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-26"
------------------------------------------------------------------------
"""
#imports
from Stack_array import Stack


values = [8,14,12,9,8,7,5]
source = Stack()

for i in values:
    source.push(i)

  
print("Source Stack:  ")
for i in source:
    print(i, end=' ')   
print("\n")

target1, target2 = source.split_alt()
print('Is_empty for source: {}\n'.format(source.is_empty()))

print("Target #1:  ")
for i in target1:
    print(i, end=' ') 
print("\n")

print("Target #2:  ")
for i in target2:
    print(i, end=' ')
print("\n")

'''
#Function .see() is in the stack_array at the bottom, if red, I greened it out for the auto-grader
print("Source Stack: {}\n".format(source.see()))
target1, target2 = source.split_alt()
print('Is_empty for source: {}\n'.format(source.is_empty()))
print("Target #1: {}".format(target1.see()))
print("Target #2: {}".format(target2.see()))
'''