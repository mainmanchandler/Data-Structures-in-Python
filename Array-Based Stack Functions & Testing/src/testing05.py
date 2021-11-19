"""
------------------------------------------------------------------------
is_palindrome_stack testing with stack
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-26"
------------------------------------------------------------------------
"""
#imports
from functions import is_palindrome_stack

#string = 'racecar'
#string = 'Otto'
#string = 'Able was I ere I saw Elba'
#string = 'A man, a plan, a canal, Panama!'
string = input()

palindrome = is_palindrome_stack(string)

print('{}'.format(palindrome))