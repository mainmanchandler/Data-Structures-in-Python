"""
------------------------------------------------------------------------
Hash_set sorted testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-04-01"
------------------------------------------------------------------------
"""
#imports
from functions import insert_words, comparison_total
from Hash_Set_sorted import Hash_Set

miserables = open('miserables.txt', 'r')
#miserables = open('paragraph.txt', 'r')

hash_set = Hash_Set(20)

insert_words(miserables, hash_set)

'''
for i in hash_set:
    print(i)
'''

#find comparisons
total, max_word = comparison_total(hash_set)


print("Using array-based Sorted List Hash_Set\n\nTotal Comparisons: {:,}\nWord with maximum comparisons '{}': {:,}".format(total, max_word.word, max_word.comparisons))






