"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-16"
-------------------------------------------------------
"""
from copy import deepcopy


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        empty = None
        
        if self._count == 0:
            empty = True
        else:
            empty = False
            
        return empty 

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        value = self._count
        return value

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if self._count > 0:
            temp = self._front
            self._front = _List_Node(value, temp)
        
        else:
            temp = _List_Node(value, None)
            self._front = temp
            self._rear = temp

        self._count += 1        
        
        return None

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        
        if self._rear is not None: 
            new_rear = _List_Node(value, None)
            self._rear._next = new_rear
            self._rear = new_rear
        
        else:
            temp = _List_Node(value, None)
            self._front = temp
            self._rear = temp


        self._count += 1

        return None

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
          
        if self._front is None:
            self.append(value)
            
        elif i <= -self._count or i == 0:
            self.prepend(value)
            
        elif i >= self._count:
            self.append(value)
        
        elif i < 0:
            new_index = self._count - abs(i)
            previous = None
            current = self._front
            j = 0
            
            while j < new_index:
                previous = current
                current = current._next
                j+=1
            
            node = _List_Node(value, current)
            previous._next = node
            
            self._count += 1
        
        else:
            
            
            previous = None
            current = self._front
            j = 0
            
            while j < i:
                previous = current
                current = current._next
                j+=1
            
            node = _List_Node(value, current)
            previous._next = node
            
            self._count += 1
        
       
        return None

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """   
         
        index = 0
        found = False
        previous = None
        current = self._front
        
        if self._count > 0:
            if self._count == 1 and current._value == key:
                found = True
            
            else:
                while not found and index < self._count:
                    if current._value == key:
                        found = True
                    
                    else:   
                        previous = current
                        current = current._next
                        index += 1

        
        if not found:
            current = None
            index = -1
         
        return previous, current, index
        
    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        previous, current, i = self._linear_search(key)
            
        if i == -1:
            value = None
            
        else:
            value = deepcopy(current._value)
            if i == 0:
                
                self._front = self._front._next
                pointer = self._front
                
                if pointer is not None:
                    
                    while pointer._next is not None:
                        pointer = pointer._next
                
                self._rear = pointer
                
            elif i == self._count - 1:
                previous = None
                pointer = self._front
                
                while pointer._next is not None:
                    previous = pointer
                    pointer = pointer._next
                
                previous._next = None
                self._rear = previous  
                
            else:
                previous._next = current._next

            self._count -= 1
        
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        
        value = deepcopy(self._front._value)
        
        if self._front._next is not None:
            self._front = self._front._next

        else:
            self._front = self._rear = None
        
        self._count -= 1
        return value 
        
        
        
        
    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        '''
        previous, current, i = self._linear_search(key)
           
        while i != -1: 
        
            if i == 0:
                
                self._front = self._front._next
                pointer = self._front
                
                if pointer is not None:
                    
                    while pointer._next is not None:
                        pointer = pointer._next
                
                self._rear = pointer
                
            elif i == self._count - 1:
                previous = None
                pointer = self._front
                
                while pointer._next is not None:
                    previous = pointer
                    pointer = pointer._next
                
                previous._next = None
                self._rear = previous  
                
            else:
                previous._next = current._next
                self._count -= 1
            
            previous, current, i = self._linear_search(key)
        
        '''
        
        index = self._linear_search(key)[2]
        
        while index != -1:
            self.pop(index)
            index = self._linear_search(key)[2]
        
        return None
        
        
    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        temp = self._linear_search(key)[1]
        if temp == None:
            value = None
        else:
            value = deepcopy(temp._value)
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        temp = self._front
        value = deepcopy(temp._value)
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        return self._linear_search(key)[2]

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
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        current = self._front
        j = 0
        
        if i < 0:
            i = self._count - abs(i)
        
        while j < i:
            current = current._next
            j += 1
            
        value = deepcopy(current._value)  
        
        return value

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        current = self._front
        j = 0
        
        if i < 0:
            i = self._count - abs(i)
        
        while j < i:
            current = current._next
            j += 1
            
        current._value = deepcopy(value)  
        
        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        
        return self._linear_search(key)[2] != -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        current = self._front
        max_data = current._value
    
        while current._next is not None:
            current = current._next   
                 
            if max_data < current._value:
                max_data = current._value
            
        return deepcopy(max_data)

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        current = self._front
        min_data = current._value
    
        while current._next is not None:
            current = current._next   
                 
            if min_data > current._value:
                min_data = current._value
            
        return deepcopy(min_data)

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        number = 0
        current = self._front
    
        while current is not None:
            if key == current._value:
                number += 1
            current = current._next
            
        return number
        

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        self._rear = self._front
        previous = None
        current = self._front

        while current is not None:
            temp = current._next
            current._next = previous
            previous = current
            current = temp

        self._front = previous
        
        return

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        self._reverse_r_aux(None, self._front)
        
        return
        
        
    def _reverse_r_aux(self, previous_node, current_node):
        
        if current_node is not None:
            temp = current_node._next
            current_node._next = previous_node
            previous_node = current_node
            current_node = temp
            
            self._reverse_r_aux(previous_node, temp)
        
        else:
            self._front = previous_node
            self._set_rear()
        
        return
        
        
    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        cleaned = List()
        current = self._front
        
        while current is not None:
            if current._value not in cleaned:
                cleaned.append(current._value)
                
            current = current._next
        
        self._front = cleaned._front
        self._count = cleaned._count
        #self._set_rear()
        self._rear = cleaned._rear
        
        return
    

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
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
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
                
        return value


    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next 
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        if pln is not prn:
            # Swap only if two nodes are not the same node

            if pln is None:
                # Make r the new front
                left = self._front
                self._front = prn._next
            else:
                left = pln._next
                pln._next = prn._next

            if prn is None:
                # Make l the new front
                right = self._front
                self._front = left
            else:
                right = prn._next
                prn._next = left

            # Swap next pointers
            # lst._next, r._next = r._next, lst._next
            temp = left._next
            left._next = right._next
            right._next = temp
            # Update the rear
            if right._next is None:
                self._rear = right
            elif left._next is None:
                self._rear = left
        return
        

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (iterative version)
        Use: b = lst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != target._count:
            identical = False
            
        else:
            source_node = self._front
            target_node = target._front

            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next

            identical = source_node is None
            
        return identical
        

    def is_identical_r(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count == target._count:
            identical = self._is_identical_r_aux(self._front, target._front)
            
        else: 
            identical = False
        
        return identical

        
    def _is_identical_r_aux(self, first, second):
        if first == None:
            identical = True
        
        elif first._value == second._value:
            identical = self._is_identical_r_aux(first._next, second._next)
        
        else:
            identical = False
        
        return identical
        
    
    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        split = self._count // 2
        
        while self._front is not None and self._count > split:
            target1._move_front_to_rear(self)
            
        while self._front is not None and self._count > 0:
            target2._move_front_to_rear(self)
            
        #print("\n\n\n",self._count)
        
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        left = True

        while self._front is not None:

            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
                
            left = not left
            
        return target1, target2
    
    
    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant. (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
    
        target1 = List()
        target2 = List()
        self._split_alt_r_aux(target1, target2)
        
        return target1, target2
        
    def _split_alt_r_aux(self, target1, target2):
        
        if self._front != None:
            target1._move_front_to_rear(self)
            
            if self._front != None:
                target2._move_front_to_rear(self)
                self._split_alt_r_aux(target1, target2)
        
        return


    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        
        return self._linear_search_aux(None, self._front, 0, key)
    
    def _linear_search_aux(self, prev, node, i, key):
        result = prev, None, -1 
        
        if node is not None:
            
            if node._value == key:
                result = prev, node, i
                
            else:
                result = self._linear_search_aux(node, node._next, i + 1, key)
        
        return result

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front

        while source1_node is not None:
            
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    # Value does not appear in target list.
                    self.append(value)

            source1_node = source1_node._next
            
        return

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._intersection_r_aux(source1._front, source2)
        return
    
    def _intersection_r_aux(self, current_node, source2):
        
        if current_node is not None:
            
            if current_node._value in source2 and current_node._value not in self:
                self.append(current_node._value)
            
            self._intersection_r_aux(current_node._next, source2)
            
        return
        
    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in new list.
                self.append(value)
            source1_node = source1_node._next

        source2_node = source2._front

        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in current list.
                self.append(value)

            source2_node = source2_node._next
        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._union_r_aux(source1._front)
        self._union_r_aux(source2._front)
        
        return None

    def _union_r_aux(self, current_node):
        if current_node is not None:
            
            if current_node._value not in self:
                self.append(current_node._value)
                
            self._union_r_aux(current_node._next)
        
        return


    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        # your code here
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = lst.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a functions that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        # your code here
        return

    def reverse_pc(self):
        """
        -------------------------------------------------------
        Reverses a list through partitioning and concatenation.
        Use: lst.reverse_pc()
        -------------------------------------------------------
        Returns:
            The contents of the current list are reversed.
        -------------------------------------------------------
        """
        # your code here
        return
    
    
    
    def _move_front(self, rs):
        """
        -------------------------------------------------------
        Moves the front node from the rs List to the front
        of the current List. Private helper method.
        Use: self._move_front(rs)
        -------------------------------------------------------
        Parameters:
            rs - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the rs List and
            its count is updated. The rs List front and count are updated.
        -------------------------------------------------------
        """
        assert rs._front is not None, \
            "Cannot move the front of an empty List"

        temp = rs._front
        rs._front = rs._front._next
        temp._next = self._front
        self._front = temp
        
        rs._set_rear()
        self._set_rear()
        
        rs._count += 1
        self._count += 1
        
        return
    
    
    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front of the list to the rear of the list.
        Private helper method.
        Use: self._move_front_to_rear(node)
        -------------------------------------------------------
        Parameters:
            target - a non-empty linked List (List)
        Returns:
            moves the front value of the list to the rear of the list
        -------------------------------------------------------
        """
        '''
        self.append(target.remove_front())
        return 
        '''
        
        assert source._front is not None, \
            "Cannot move the front of an empty List"
        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next
        if source._front is None:
            # Clean up source list if empty.
            source._rear = None
        # Update the target list
        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node
        node._next = None
        self._rear = node
        self._count += 1
        return
    
    def _set_rear(self):
        """
        -------------------------------------------------------
        Sets the rear of the list from the front of the list.
        Private helper method, helps retrieve the rear.
        Use: self._set_rear()
        -------------------------------------------------------
        Returns:
            finds the rear of the list and sets self._rear
        -------------------------------------------------------
        """
        current = self._front
        
        if current == None:
            self._rear = None
            
        else:
            while current._next is not None:
                current = current._next
            
            self._rear = current
                
        return
     
    
    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        altn = True
        
        while source1._front is not None or source2._front is not None:

            if altn and source1._count > 0:
                self._move_front_to_rear(source1)
    
            elif not altn and source2._count > 0:
                self._move_front_to_rear(source2)

            altn = not altn

        while source1._front is not None:
            self._move_front_to_rear(source1)
         
        while source2._front is not None:
            self._move_front_to_rear(source2)
            
        self._set_rear()

        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
