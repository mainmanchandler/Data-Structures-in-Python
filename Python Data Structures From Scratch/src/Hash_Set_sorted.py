"""
-------------------------------------------------------
Sorted-based list version of the Hash Set ADT.
-------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2019-04-27"
-------------------------------------------------------
"""
# Imports
# Use any appropriate data structure here.
from Sorted_List_array import Sorted_List
# Define the new_slot slot creation functions.
new_slot = Sorted_List

# Constants
SEP = '-' * 40


class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, slots):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of size slots.
        Use: hs = Hash_Set(slots)
        -------------------------------------------------------
        Parameter:
            slots - number of initial slots in Hash Set (int > 0)
        Returns:
            A new Hash_Set object (Hash_Set)
        -------------------------------------------------------
        """
        self._slots = slots
        self._table = []
        self._count = 0

        # Define the empty slots.
        for _ in range(self._slots):
            self._table.append(new_slot())

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot(key)
        -------------------------------------------------------
        Returns:
            slot - list at the position of hash key in self._table
        -------------------------------------------------------
        """
        
        slot = self._table[hash(key) % self._slots]
        
        return slot


    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """
        #not functional
        contains = False
        if key in self._table:
            contains = True
        
        return contains

    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the Hash Set, allows only one copy of value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        inserted = False
        i_slot = self._find_slot(value)
        
        if value not in i_slot:
            inserted = True
            i_slot.insert(value)
            self._count += 1
            
            if self._count > Hash_Set._LOAD_FACTOR * self._slots:
                self._rehash()
                
        return inserted
        
        
    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        value = slot.find(key)
        
        return value
    
    	
    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """        
        list_slot = self._find_slot(key)
        value = list_slot.remove(key)
        
        if value != None:
            self._count -= 1 
        
        
        return value
        

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        temp = self._table
        self._slots = self._slots * 2 + 1
        self._table = []
        
        for _ in range(self._slots):
            self._table.append(new_slot())
             
        while len(temp) != 0:
            prev_slot = temp.pop() #prev as in like the old table slot
            
            while not prev_slot.is_empty():
                val = prev_slot.pop()
                i_slot = self._find_slot(val)
                i_slot.insert(val)
                  
        return
        
    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two hash sets are identical.
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
             target - another hash set (Hash_Set)
        Returns:
            identical - True if this hash set contains the same values 
                as other in the same order, otherwise returns False.
        -------------------------------------------------------
        """

        # your code here


    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        print("{} slots\n".format(self._slots))
        print("========================================")
        
        for i_slot in range(self._slots):
            print("\nSlot {}".format(i_slot))
            
            for val in self._table[i_slot]:
                print(val)
        
        return


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item
