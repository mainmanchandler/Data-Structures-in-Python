"""
------------------------------------------------------------------------
Functions file for Hash_set word comparisons
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-04-01"
------------------------------------------------------------------------
"""
#imports
from Word import Word

def insert_words(fv, hash_set):
    """
    -------------------------------------------------------
    Retrieves every Word in fv and inserts into
    a Hash_Set.
    Each Word object in hash_set contains the number of comparisons
    required to insert that Word object from file_variable into hash_set.
    Use: insert_words(fv,hash_set)
    -------------------------------------------------------
    Parameters:
        fv - the already open file containing data to evaluate (file)
        hash_set - the Hash_Set to insert the words into (Hash_Set)
    Returns:
        None
    -------------------------------------------------------
    """
    line = fv.readline()
    
    while line != '':
        line = line.split()
        
        for i in line:
            if i.isalpha():
                word = Word(i.lower())
                hash_set.insert(word)    
        
        line = fv.readline()
    
    return



def comparison_total(hash_set):
    """
    -------------------------------------------------------
    Sums the comparison values of all Word objects in hash_set.
    use: total, max_word = comparison_total(hash_set)
    -------------------------------------------------------
    Parameters:
        hash_set - a hash set of Word objects (Hash_Set)
    Returns:
        total - the total of all comparison fields in the Hash_Set
            Word objects (int)
        max_word - the word having the most comparisons (Word)
    -------------------------------------------------------
    """
    total = 0
    max_word = None
    max_comparison = -1
    
    for word in hash_set:
        total += word.comparisons
        
        if word.comparisons > max_comparison:
            max_word = word
            max_comparison = word.comparisons
    
    
    return total, max_word









