"""
-------------------------------------------------------
Array version of the list ADT.
-------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-16"
-------------------------------------------------------
"""
from copy import deepcopy

class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: target = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._values = []


    def __getitem__(self, i):
        """
        -------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'
        
        value = deepcopy(self._values[i])
        return value


    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        
        return len(self._values)


    def __setitem__(self, i, value):
        """
        -------------------------------------------------------
        The i-th element of list contains a copy of value. The existing
        value at i is overwritten.
        Use: source[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'
        
        self._values[i] = deepcopy(value)
        return 


    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        return self._linear_search(key) != -1 #linear search through the list to see if the list has the key


    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        # -length is less than or equal to the index and the index is less the the total length
        
        return -len(self) <= i < len(self) 


    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of key in the list, -1 if key is not found (int)
        -------------------------------------------------------
        """
        
        i = -1
        iterator = 0
        
        while i == -1 and iterator < len(self):
            
            if self._values[iterator] == key:
                i = iterator
            
            iterator += 1
        
        return i


    def _swap(self, i, j):
        """
        -------------------------------------------------------
        Swaps the position of two elements in the data list.
        The element originally at position i is now at position j,
        and visa versa.
        Private helper operations called only from within class.
        Use: self._swap(i, j)
        -------------------------------------------------------
        Parameters:
            i - index of one element to switch (int, 0 <= i < len(self._values))
            j - index of other element to switch (int, 0 <= j < len(self._values))
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index i'
        assert self._is_valid_index(j), 'Invalid index j'

        swap1 = deepcopy(self._values[i])
        swap2 = deepcopy(self._values[j])
        self._values[i] = swap2
        self._values[j] = swap1

        return


    def append(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: source.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        return None


    def apply(self, func):
        """
        -------------------------------------------------------
        Applies an external functions to every value in list.
        Use: source.apply(func)
        -------------------------------------------------------
        Parameters:
          func - a functions that takes a single value as a parameter 
              and returns a value (functions)
        Returns:
            None
        -------------------------------------------------------
        """
        for i in self._values:
            func(i)
        
        return None


    def clean(self):
        """
        ---------------------------------------------------------
        The list contains one and only one of each value formerly present
        in the list. The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        clean_list = []
        
        for i in self._values:
            if i not in clean_list:
                clean_list.append(i)
        
        self._values = clean_list
        
        return None


    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (List)
            source2 - an array-based list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        altn = True
        
        max_run = len(source1) + len(source2)
        run = 0

        while len(self._values) < max_run:
            
            if altn and not source1.is_empty():
                self._values.append(source1.pop(0))

                
            elif not altn and not source2.is_empty():
                self._values.append(source2.pop(0))

            altn = not altn
            run += 1
        
        return None


    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a copy of self (List)
        -------------------------------------------------------
        """
        
        target = deepcopy(self)
        return target


    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        number = 0
        
        for i in self._values: #performs the same linear search as _linear_search
            if i == key:
                number += 1
        
        return number


    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        i = self._linear_search(key)
        
        if i == -1: #if the key is not found
            value = None
            
        else:
            value = deepcopy(self._values[i]) #found the location of the key
        
        return value


    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list. (int)
        -------------------------------------------------------
        """
        i = self._linear_search(key)
        
        return i


    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: source.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        
        if i < -len(self):
            self._values.insert(0, deepcopy(value))
            
        elif i >= len(self):
            self._values.insert(i, deepcopy(value))
        
        else:
            self._values.insert(i, deepcopy(value))
                                
        return None


    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (List)
            source2 - an array-based list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        for i in source1:
            if i in source2 and i not in self._values:
                self._values.append(i)
                
        for i in source2:
            if i in source1 and i not in self._values:
                self._values.append(i)
                
        return None


    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """

        return len(self._values) == 0


    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are is_identical, i.e. same values 
        appear in the same locations in both lists. 
        (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        n = 0
        identical = len(self._values) == len(target) #Set boolean to whether the length of both lists are equal
        
        while n < len(self) and identical: #if the above case is true, check for all values
            identical = self[n] == target[n]
            n += 1    
                
        return identical


    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find maximum of an empty list'
        
        value = self._values[0]
        
        for value_at_index in self._values:
            if value_at_index > value:
                value = value_at_index
        
        return deepcopy(value)


    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find minimum of an empty list'

        value = self._values[0]
        
        for value_at_index in self._values:
            if value_at_index < value:
                value = value_at_index
        
        return deepcopy(value)


    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty list'
        
        value = deepcopy(self._values[0])
        return value


    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            # pop the element at position i
            i = args[0]
            value = self._values.pop(i)
        else:
            # pop the last element
            value = self._values.pop()
        return value


    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: source.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        updated_list = [value] #sets the first value to the new value
        
        for i in self._values:
            updated_list.append(i) #adds the old list to the new one
            
        self._values = updated_list #makes the old one the new one
        
        return


    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        
        i = self._linear_search(key)
        
        if i > -1:
            value = deepcopy(self._values[i])
            self._values.remove(value)
        else:
            value = None
            
        return value


    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty list'
        
        value = self._values.pop(0)
        
        return value


    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: source.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        run = True
        
        while run:
            
            i = self._linear_search(key)
            
            if i != -1:
                self._values.remove(key)
                
            else:
                run = False        
            
        return None
        

    def reverse(self):
        """
        -------------------------------------------------------
        The contents of list are reversed in order with respect
        to their order before the operation was called.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        for i in range(len(self._values) // 2):
            reversal1 = self._values[i]
            reversal2 = self._values[-i -1]
            self._values[i] = reversal2
            self._values[-i -1] = reversal1

        
        return None


    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """

        target1 = List()
        target2 = List()
        split = len(self._values) // 2
        
        while len(self._values) > split:
            target1._values.append(self._values.pop(0))

        while len(self._values) > 0:
            target2._values.append(self._values.pop(0))

        return target1, target2
           
    
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """

        target1 = List()
        target2 = List()
        altn = True
        
        while len(self._values) > 0:
            
            if(altn):
                target1._values.append( self._values.pop(0) )

            else:
                target2._values.append( self._values.pop(0) )

            altn = not altn

        return target1, target2

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = source.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a functions that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        # Your code here

        return


    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values < key,
        and target2 contains all values >= key.
        Use: target1, target2 = source.split_key()
        -------------------------------------------------------
        Returns:
            target1 - a new List of values < key (List)
            target2 - a new List of values >= key (List)
        -------------------------------------------------------
        """
        # Your code here

        return


    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (List)
            source2 - an array-based list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        
        for i in source1:
            if i not in self._values:
                self._values.append(i)
                
        for i in source2:
            if i not in self._values:
                self._values.append(i)
                
        return None

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns:
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

