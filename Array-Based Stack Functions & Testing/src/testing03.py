"""
------------------------------------------------------------------------
Stack_combine testing from Functions
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-26"
------------------------------------------------------------------------
"""
#imports
from functions import stack_combine
from Stack_array import Stack

values1 = [8,12,8,5]
values2 = [14,9,7,1,6,3]

#values1.reverse()
#values2.reverse()

source1 = Stack()
source2 = Stack()

for i in values1:
    source1.push(i)
    
for i in values2:
    source2.push(i)



#Output
print("Source Stack #1:  ")
for i in source1:
    print(i, end=' ')   
print("\n")

print("Source Stack #2:  ")
for i in source2:
    print(i, end=' ')   
print("\n")


target = stack_combine(source1, source2)
print('Is_empty for source1: {}\n'.format(source1.is_empty()))
print('Is_empty for source2: {}\n'.format(source2.is_empty()))


print("Target:  ")
for i in target:
    print(i, end=' ') 
print("\n")

'''
target.pop()
print("Target:  ")
for i in target:
    print(i, end=' ') 
print("\n")
'''



'''
#Function .see() is in the stack_array at the bottom, if red, I greened it out for the auto-grader
print("Source Stacks: \n{}\n{}\n".format(source1.see(),source2.see()))
target = stack_combine(source1, source2)
print('Is_empty for source1: {}\n'.format(source1.is_empty()))
print('Is_empty for source2: {}\n'.format(source2.is_empty()))
print("Target #1: {}".format(target.see()))
'''
