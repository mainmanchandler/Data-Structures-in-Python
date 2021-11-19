"""
------------------------------------------------------------------------
Array version of the stack ADT.
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-21"
------------------------------------------------------------------------
"""
from copy import deepcopy


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an is_empty stack. Data is stored in a Python list.
        Use: s = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Returns:
            True if the stack is empty, False otherwise
        -------------------------------------------------------
        """
        empty_check = len(self._values)
        check_result = False
        
        #if the stack/list is empty (ie == 0)
        if empty_check == 0:
            check_result = True
            
        return check_result

        
    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: s.push(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        
        return None
        


    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = s.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty stack"
        
        value = self._values.pop()
        
        return value
        

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"
        
        value = deepcopy(self._values[-1])
        
        return value


    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value



    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values
        alternating into the targets. At finish source stack is empty.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        '''
        ---Push:---
        self._values.append(deepcopy(value))

        ---Pop:---
        self._values.pop()
        
        ---Empty:---
        len(self._values) == 0
        
        '''
        assert len(self._values) > 0, "Cannot peek at an empty stack"        
        
        target1 = Stack()
        target2 = Stack()
        left = True

        while len(self._values) > 0:

            if left:
                target1._values.append(self._values.pop())
            else:
                target2._values.append(self._values.pop())
            left = not left
            
        return target1, target2
    
    
    
    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based stack (Stack)
            source2 - an array-based stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        '''
        ---Push:---
        self._values.append(deepcopy(value))

        ---Empty:---
        len(self._values) == 0
        
        '''
        
        altn = True
        
        case1 = False
        case2 = False
        
        while not case1 and not case2:
            if source1.is_empty():
                case1 = True
            if source2.is_empty():
                case2 = True
    
    
            if altn and not source1.is_empty():
                self._values.append(source1.pop())
                altn = False
                
            elif altn == False and (not source2.is_empty()):
                self._values.append(source2.pop())
                altn = True
    
        if case1 == False:
            for i in source1:
                self._values.append(source1.pop())
                
        elif case2 == False:
            for i in source2:
                self._values.append(source2.pop())
        
        
        
        return None
        
    
    
    
    '''
    def see(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to see an empty stack throws an exception.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot see an empty stack"
        
        value = deepcopy(self._values)
        return value
    '''
            
            