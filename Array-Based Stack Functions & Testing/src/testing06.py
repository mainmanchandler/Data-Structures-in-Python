"""
------------------------------------------------------------------------
Postfix from functions testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-26"
------------------------------------------------------------------------
"""
#imports
from functions import postfix

#string = '12 5 -' # = 7
#string = '4 5 + 12 * 2 3 * -' # = 102
string = '8'

answer = postfix(string)
print(type (answer))
print(answer)



