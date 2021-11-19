"""
------------------------------------------------------------------------
functions testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-03-09"
------------------------------------------------------------------------
"""
#imports
from Letter import Letter

 
def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    line = file_variable.readline()
    
    while line != '':
        line = line.strip()
        i = 0
        while len(line) > i:
            if line[i].isalpha():
                letter = Letter(line[i].upper())
                bst.retrieve(letter)
            i += 1
        line = file_variable.readline()
    return
 

def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = _aux_comparison_total(bst._root)
    return total
 
 
def _aux_comparison_total(node):
    if node is not None:
        sum =  node._value.comparisons + _aux_comparison_total(node._left) + _aux_comparison_total(node._right)
    else:
        sum = 0
 
    return sum
 


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    list = bst.inorder()
    total_count = 0
    
    i = 0
    while i < len(list):
        total_count += list[i].count
        i += 1
    
    print('Letter Count/Percent Table\n\nTotal Count: {:,}\n\nLetter  Count       %\n---------------------'.format(total_count))
    
    i = 0
    while i < len(list):
        print('   {}  {:7,} {:7,.2%}'.format(list[i].letter,list[i].count,list[i].count/total_count))
        i += 1
    
    return











