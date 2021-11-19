"""
------------------------------------------------------------------------
testing letter table function
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-03-09"
------------------------------------------------------------------------
"""
#imports
from functions import letter_table
from BST_linked import BST
from functions import do_comparisons, comparison_total
from Letter import Letter


DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
    
#delete initial comparisions:
for letter in bst1:
    letter.comparisons = 0


do_comparisons(miserables, bst1)
total = comparison_total(bst1)

letter_table(bst1)






