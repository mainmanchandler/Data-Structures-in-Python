"""
------------------------------------------------------------------------
priority_queue_linked testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-03-08"
------------------------------------------------------------------------
"""
#imports
from Priority_Queue_linked import Priority_Queue

print("--split_alt testing--")
source = [3,2,4,5,1,1]
que = Priority_Queue()

print(source)
for i in source:
    que.insert(i)
for i in que:
    print(i, end=" ")

print()
tar1, tar2 = que.split_alt()
for i in tar1:
    print(i, end=" ")
print()
for i in tar2:
    print(i, end=" ")



print('\n\n')
print("--split_key testing--")
source = [3,2,4,5,1,1,7,56,4,32,]
que = Priority_Queue()
key = 3


print(source)
for i in source:
    que.insert(i)
for i in que:
    print(i, end=" ")

print()
tar1, tar2 = que.split_key(key)
for i in tar1:
    print(i, end=" ")
print()
for i in tar2:
    print(i, end=" ")
    
    
    
print('\n\n')
print("--combine testing--")
source1=[11,33,55]
source2=[22,44,66]
print("input sources:")
print(source1)
print(source2)
print()


que1 = Priority_Queue()
que2 = Priority_Queue()
target = Priority_Queue()
for i in source1:
    que1.insert(i)
for i in source2:
    que2.insert(i)


target.combine(que1,que2)

for i in target:
    print(i, end=' ')
