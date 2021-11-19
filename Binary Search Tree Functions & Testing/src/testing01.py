"""
------------------------------------------------------------------------
testing for all bst functions
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-03-09"
------------------------------------------------------------------------
"""
#imports
from BST_linked import BST

bst = BST()
values = [11,7,15,6,9,12,18,8]
#values = [11,10,9,8,7,5,4,3]
for i in values:
    bst.insert(i)

print("-----default testing bst:-----") 
for i in bst:
    print(i, end=" ")





print("\n\n\n---Is_balanced Testing---\n")

balanced = bst.is_balanced()
print("unbalanced bst:", balanced)

bst_balanced = BST()
values = [11,7,15,6,9,12,18]
for i in values:
    bst_balanced.insert(i)
    
balanced = bst_balanced.is_balanced()
print("balanced bst:", balanced)





print("\n\n\n---Is_valid Testing---\n")
print('working in online testing')




print("\n\n\n---Is_identical Testing---\n")
print('working in online testing')



print("\n\n\n---Min Testing---\n")

value = bst.min()
print("smallest value in default bst:", value)



print("\n\n\n---leaf_count Testing---\n")
count = bst.leaf_count()
print("valid in online testing: ", count)


print("\n\n\n---one_child_count Testing---\n")
count = bst.one_child_count()
print('from the default bst: ', count)


print("\n\n\n---two_child_count Testing---\n")
count = bst.two_child_count()
print('from the default bst: ', count)



print("\n\n\n---Inorder Testing---\n")
a = bst.inorder()
print(a)

print("\n\n\n---Preorder Testing---\n")
a = bst.preorder()
print(a)




print("\n\n\n---Postorder Testing---\n")
a = bst.postorder()
print(a)




print("\n\n\n---Levelorder Testing---\n")
a = bst.levelorder()
print(a)



print("\n\n\n---Remove Testing---\n")

a = bst.inorder()
print(a)


value = bst.remove(9)
a = bst.inorder()
print('removed 9:\n ',a)

value = bst.remove(7)
a = bst.inorder()
print('removed 7:\n ',a)

value = bst.remove(11)
a = bst.inorder()
print('removed 11:\n ',a)









