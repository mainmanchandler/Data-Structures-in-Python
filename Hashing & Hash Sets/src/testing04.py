"""
------------------------------------------------------------------------
BST method testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-04-02"
------------------------------------------------------------------------
"""
#imports
from BST_linked import BST


bst = BST()

values = [11,7,15,6,9,12,18,8]
for i in values:
    bst.insert(i)

print("-----default testing bst:-----") 
for i in bst:
    print(i, end=" ")



print("\n\n-----node_counts:-----") 
zero, one, two = bst.node_counts()
print(zero)
print(one)
print(two)



print("\n-----__contains__:-----") 
key = 9
b = key in bst
print('with 9',b)
key = 24
b = key in bst
print('with 24',b)



print("\n-----parent (iterative):-----") 
key = 7
value = bst.parent(key)
print("parent value before 7: {}".format(value))

key = 9
value = bst.parent(key)
print("parent value before 9: {}".format(value))

key = 12
value = bst.parent(key)
print("parent value before 12: {}".format(value))

key = 15
value = bst.parent(key)
print("parent value before 15: {}".format(value))

key = 88
value = bst.parent(key)
print("parent value before 88: {}".format(value))

key = 11
value = bst.parent(key)
print("parent value before 11: {}".format(value))



print("\n-----parent_r (recursive):-----") 
key = 7
value = bst.parent_r(key)
print("parent value before 7: {}".format(value))

key = 9
value = bst.parent_r(key)
print("parent value before 9: {}".format(value))

key = 12
value = bst.parent_r(key)
print("parent value before 12: {}".format(value))

key = 15
value = bst.parent_r(key)
print("parent value before 15: {}".format(value))

key = 88
value = bst.parent_r(key)
print("parent value before 88: {}".format(value))

key = 11
value = bst.parent_r(key)
print("parent value before 11: {}".format(value))








