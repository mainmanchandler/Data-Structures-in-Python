"""
------------------------------------------------------------------------
testing efficiency of the data sets in function
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-03-09"
------------------------------------------------------------------------
"""
#imports
from functions import do_comparisons, comparison_total
from BST_linked import BST
from Letter import Letter

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

miserables = open('decline.txt', 'r')
#miserables = open('miserables.txt', 'r')
#miserables = open('paragraph.txt', 'r')


bst1 = BST()

for i in DATA1:
    bst1.insert(Letter(i))

'''
for i in bst1:
    print(i,end=" ")
'''
    
#delete initial comparisons:
for letter in bst1:
    letter.comparisons = 0


do_comparisons(miserables, bst1)
total = comparison_total(bst1)

print('Comparing by Order: {}'.format(DATA1))
print("Total Comparisons: {:,}".format(total))



print('-----------------------------------------------------')



miserables = open('miserables.txt', 'r')
#miserables = open('paragraph.txt', 'r')


#fill the bst with data letters
bst2 = BST()
for i in DATA2:
    bst2.insert(Letter(i))

'''
for i in bst2:
    print(i,end=" ")
'''
    
#delete initial comparisons:
for letter in bst2:
    letter.comparisons = 0

do_comparisons(miserables, bst2)
total = comparison_total(bst2)

print('Comparing by Order: {}'.format(DATA2))
print("Total Comparisons: {:,}".format(total))


print('-----------------------------------------------------')



miserables = open('miserables.txt', 'r')
#miserables = open('paragraph.txt', 'r')


#fill the bst with data letters
bst3 = BST()
for i in DATA3:
    bst3.insert(Letter(i))

'''
for i in bst3:
    print(i,end=" ")
'''

#delete initial comparisons:
for letter in bst3:
    letter.comparisons = 0

do_comparisons(miserables, bst3)
total = comparison_total(bst3)

print('Comparing by Order: {}'.format(DATA3))
print("Total Comparisons: {:,}".format(total))



