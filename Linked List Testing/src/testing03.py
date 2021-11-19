"""
------------------------------------------------------------------------
Deque_linked testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-03-08"
------------------------------------------------------------------------
"""
#imports
from Deque_linked import Deque, _Deque_Node

print("--insert_rear testing--")
source = [3,2,4,5,1,1,7,56,4,32]
deq = Deque()

for i in source:
    deq.insert_rear(i)

for i in deq:
    print(i, end=" ")
    
    
print('\n\n')
print("--insert_front testing--")

deq.insert_front(source[0])
deq.insert_front(source[1])
deq.insert_front(source[2])

for i in deq:
    print(i, end=" ")



print('\n\n')
print("--remove_front testing--")

print(deq.remove_front())

for i in deq:
    print(i, end=" ")



print('\n\n')
print("--remove_rear testing--")

print(deq.remove_rear())

for i in deq:
    print(i, end=" ")
    

print('\n\n')
print("--_swap method testing--")
source = [0,1,2,3]
deq = Deque()

for i in source:
    deq.insert_rear(i)
for i in deq:
    print(i, end=" ")

print('\n')
node1 = deq._front._next #1
node2 = deq._rear._prev #2

print("\nswapping index {} with {}".format(1,2))
deq._swap(node1,node2)

for i in deq:
    print(i, end=" ")


node1 = deq._front #0
node2 = deq._rear._prev #2

print("\nswapping index {} with {}".format(0,2))
deq._swap(node1,node2)

for i in deq:
    print(i, end=" ")


node1 = deq._front._next #1
node2 = deq._rear #3

print("\nswapping index {} with {}".format(1,3))
deq._swap(node1,node2)

for i in deq:
    print(i, end=" ")
