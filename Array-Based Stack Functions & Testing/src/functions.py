"""
------------------------------------------------------------------------
Assignment #3 - Functions File
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-26"
------------------------------------------------------------------------
"""
#imports
from Stack_array import Stack

#constants
VALID_CHAR = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
OPERATORS = "+-*/"

def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    
    altn = True
    
    while not source.is_empty():
        if altn:
            target1.push(source.pop())
            altn = False
        else:
            target2.push(source.pop())
            altn = True

    
    return target1, target2




def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    
    target = Stack()    
    altn = True
    
    case1 = False
    case2 = False
    
    while not case1 and not case2:
        if source1.is_empty():
            case1 = True
        if source2.is_empty():
            case2 = True


        if altn and not source1.is_empty():
            target.push(source1.pop())
            altn = False
            
        elif altn == False and (not source2.is_empty()):
            target.push(source2.pop())
            altn = True


    if case1 == False:
        for i in source1:
            target.push(source1.pop())
            
    elif case2 == False:
        for i in source2:
            target.push(source2.pop())
    
    return target
    
    
    
    
    
def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    stack = Stack()
    no_val_char = True
    forward_string = ''
    
    if len(string) == 0:
        palindrome = True
        
    else:
        
        for char in string:
            if char in VALID_CHAR:
                stack.push(char)  
                forward_string += char  
                no_val_char = False   
        
        
        reversed_string = ''
        
        if no_val_char:
            palindrome = False
            
        else:
            
            while not stack.is_empty():
                reversed_string += stack.pop()
                
            
            if forward_string.lower() == reversed_string.lower():
                palindrome = True
            else:
                palindrome = False
            
            #print(forward_string.lower())
            #print(reversed_string.lower())
    
    return palindrome
    





def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    
    stack = Stack()
    
    new_string = string.split()
    #print(new_string)

    for i in new_string:
        
        if i in OPERATORS:
            second_op = stack.pop()
            first_op = stack.pop()
            
            if i == OPERATORS[0]:
                resultant = first_op + second_op
                
            elif i == OPERATORS[1]:
                resultant = first_op - second_op
                
            elif i == OPERATORS[2]:
                resultant = first_op * second_op
            
            elif i == OPERATORS[3]:
                resultant = first_op / second_op

            stack.push(resultant)
            
        else:
            stack.push(float(i))
    
    
    
    answer = stack.pop()
    #print(stack.is_empty())
    
    return float(answer)
    
    


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points ~visited~ (not started) before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    path = []
    stack = Stack()
    exit = False

    stack.push('Start')
    
    while not exit and not stack.is_empty():
        
        next_stop = stack.pop()

        if next_stop != 'Start':
            path.append(next_stop)
        
        stops = maze[next_stop]
        
        if 'X' in stops:
            path.append('X')
            exit = True
        
        else:
            for i in stops:
                stack.push(i)
               
               
    if 'X' not in path:
        path = None      
            
    return path




