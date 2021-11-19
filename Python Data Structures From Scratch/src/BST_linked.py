"""
-------------------------------------------------------
Linked version of the BST ADT.
-------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2019-04-27"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers 
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            A _BST_Node object (_BST_Node)            
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched. Updates structure of bst as 
        required.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value matching key if found, otherwise None.
        -------------------------------------------------------
        """
        self._root, value = self._remove_aux(self._root, key)
        return value

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Parameters:
            node - a bst node to search for key (_BST_Node)
            key - data to search for (?)
        Returns:
            node - the current node or its replacement (_BST_Node)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            # Base Case: the key is not in the tree.
            value = None
        elif key < node._value:
            # Search the left subtree.
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._value:
            # Search the right subtree.
            node._right, value = self._remove_aux(node._right, key)
        
        else:
            # Value has been found.
            value = node._value
            self._count -= 1
            
            # Replace this node with another node.
            if node._left is None and node._right is None:
                # node has no children.
                node = None
                
            elif node._left is None:
                # node has no left child.
                node = node._right

            elif node._right is None:
                # node has no right child
                node = node._left
            
            else:
                # Node has two children
                if node._left._right is None:
                    rep_node = node._left
                else:
                    rep_node = self._delete_node_left(node._left)
                    rep_node._left = node._left
                    
                rep_node._right = node._right
                node = rep_node    
                
        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
            
        return node, value
    
    
    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            parent - node to search for largest value (_BST_Node)
        Returns:
            repl_node - the node that replaces the deleted node. This node 
                is the node with the maximum value in the deleted node's left
                subtree (_BST_Node)
        -------------------------------------------------------
        """
            
        if parent._right._right is None:
            repl_node = parent._right
            parent._right = parent._right._left
        else:
            repl_node = self._delete_node_left(parent._right)

        
        return repl_node



    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """
        contains = False
        
        v = self.retrieve(key)
        if v is not None:
            contains = True
            
        return contains

    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            maximum height of bst (int)
        -------------------------------------------------------
        """
        max_height = 0
        node = self._root
        
        if self._root is not None:
            max_height = node._height
        return max_height
        


    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are identical.
        Use: b = bst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another bst (BST)
        Returns:
            identical - True if this bst contains the same values
            in the same order as other, otherwise returns False (boolean)
        -------------------------------------------------------
        """
        node_one = self._root
        node_two = other._root
        identical = self._is_identical_aux(node_one, node_two)

        return identical
    
    
    def _is_identical_aux(self, node_one, node_two):
        """
        ---------------------------------------------------------
        aux functions for is_identical (recursive)
        Use: b = bst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            node_one - root node of self (node)
            node_two - root node of other (node)
        Returnst
            identical - True if this bst contains the same values
            in the same order as other, otherwise returns False (boolean)
        -------------------------------------------------------
        """
        
        if node_one is None and node_two is None:
            identical = True
            
        elif node_one is None or node_two is None:
            identical = False
            
        elif node_one._value != node_two._value:
            identical = False
        
        else:
        
            identical = self._is_identical_aux(node_one._left, node_two._left) and self._is_identical_aux(node_one._right, node_two._right)
        
        
        return identical


    def parent(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        Use: value = bst.parent(key)
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"
        
        if self._root:
            temp = []
            temp.append(self._root)
            value = None 
            
            if self._root._value == key:
                value = None
            
            else:
                while len(temp) > 0 and value == None:
                    node = temp.pop(0)
                
                    if node._left:
                        temp.append(node._left)
                        if node._left._value == key:
                            value = deepcopy(node._value)
                            
                    if node._right:
                        temp.append(node._right)
                        if node._right._value == key:
                            value = deepcopy(node._value)
        
        return value


    def parent_r(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        Use: value = bst.parent_r(key)
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"
        
        temp = None
        if self._root is not None:
            value = deepcopy(self._parent_r_aux(key, self._root, temp))
        else:
            value = None
        return value


    def _parent_r_aux(self, key, node, temp):
        
        if node is not None:
            if node._right is not None and node._right._value == key:
                temp = node._value
            
            elif node._left is not None and node._left._value == key:
                temp = node._value
            
            else:
                temp = self._parent_r_aux(key, node._left, temp) or self._parent_r_aux(key, node._right, temp)
        
        return temp


    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        # your code here


    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"
        
        node = self._root
        max_node = self._max_r_aux(node)
        value = max_node._value
        
        return value
        
    def _max_r_aux(self, max_node):
        """
        ---------------------------------------------------------
        aux functions for max_r 
        Use: value = self._max_r_aux()
        ---------------------------------------------------------
        Parameter:
            node - self._root (node)
        Returns:
            node - a copy of the maximum value node in the BST (?)
        ---------------------------------------------------------
        """
        
        if max_node is not None and max_node._right is not None:
            max_node = self._max_r_aux(max_node._right)
        
        return max_node


    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in BST. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"
        value = None
        node = self._root
        
        while node != None:
            value = node._value
            node = node._left 
        
        return value

    def min_r(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        node = self._root
        min_node = self._min_r_aux(node)
        value = min_node._value
        
        return value
    

    def _min_r_aux(self, min_node):
        """
        ---------------------------------------------------------
        aux functions for min_r 
        Use: value = self._max_r_aux()
        ---------------------------------------------------------
        Parameter:
            node - self._root (node)
        Returns:
            node - a copy of the maximum value node in the BST (?)
        ---------------------------------------------------------
        """
        
        if min_node is not None and min_node._left is not None:
            min_node = self._min_r_aux(min_node._left)
        
        return min_node

    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: count = bst.leaf_count()
        ---------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        node = self._root
        count = 0
        count = self._leaf_count_aux(node, count)
        
        return count
        
    def _leaf_count_aux(self, node, temp_count):
        
        count = None
        
        if node is None:
            count = 0
        else:
            if node._left is None and node._right is None:
                temp_count += 1
            else:
                temp_count = self._leaf_count_aux(node._left, temp_count) + self._leaf_count_aux(node._right, temp_count)
        
            count = temp_count
        
        return count


    def two_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """
        count = self._two_child_count_aux(self._root)
        return count
        
    def _two_child_count_aux(self, node):
        if node is None:
            count = 0
            
        elif node._left is not None and node._right is not None:
            count = 1 + self._two_child_count_aux(node._left) +  self._two_child_count_aux(node._right)
            
        else:
            count = self._two_child_count_aux(node._left) + self._two_child_count_aux(node._right)
        
        return count
        

    def one_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """
        count = self._one_child_count_aux(self._root)
        
        return count
        
    def _one_child_count_aux(self, node):
        if node is None:
            count = 0
        
        elif node._left is not None and node._right is None:
            count = 1 + self._one_child_count_aux(node._left) +  self._one_child_count_aux(node._right)
            
        elif node._left is None and node._right is not None:
            count = 1 + self._one_child_count_aux(node._left) +  self._one_child_count_aux(node._right)
            
        else:
            count = self._one_child_count_aux(node._left) + self._one_child_count_aux(node._right)
        
        return count


    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """
        zero = self.leaf_count()
        one = self.one_child_count()
        two = self.two_child_count()
        
        return zero, one, two


    def total_depth(self):
        """
        ---------------------------------------------------------
        Returns the total depth of a bst.
        ---------------------------------------------------------
        Returns:
            the total depth count - i.e. the sum of all the node depths
            in the tree (int)
        ---------------------------------------------------------
        """

        # your code here


    def mirror(self):
        """
        ---------------------------------------------------------
        Creates a mirror version of a BST. All nodes are swapped with nodes on
        the other side the tree. Nodes may take the place of an empty spot.
        The resulting tree is a mirror image of the original tree. (Note that
        the mirrored tree is not a BST.) The original BST is unchanged.
        Use: tree = bst.mirror()
        ---------------------------------------------------------
        Returns:
            tree - a mirror version of subtree of node.
        ---------------------------------------------------------
        """

        # your code here


    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        node = self._root
        balanced = None
        
        if node is None:
            balanced = True
        else:
            balanced = self._is_balanced_aux(node)
        
        return balanced
        
        
    def _is_balanced_aux(self, node):
        """
        ---------------------------------------------------------
        is_balanced_aux functions (private)
        
        Use: b = bst._is_balanced_aux()
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        balanced = None
        
        if node._left is None and node._right is None:
            balanced = True
            
        elif node._left is None or node._right is None:
            balanced = False
            
        elif abs(node._left._height - node._right._height) > 0:
            balanced = False
            
        else:
            balanced = self._is_balanced_aux(node._left) and self._is_balanced_aux(node._right)
        
        return balanced
        
        

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper functions to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """

        # your code here


    def average_depth(self):
        """
        ---------------------------------------------------------
        Returns the average depth of a bst.
        ---------------------------------------------------------
        Returns:
            avg-depth - total depth count divided by the number of nodes
                in the tree (int)
        ---------------------------------------------------------
        """

        # your code here


    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        node = self._root
        valid = self._is_valid_aux(node)
        
        return valid

    def _is_valid_aux(self, node):
        """
        ---------------------------------------------------------
        aux functions for is_valid (recursive)
        Use: valid = self._is_valid_aux(node)
        ---------------------------------------------------------
        Parameters:
            node - root of bst (node)
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        
        if node is not None:
            
            if node._left is None:
                left_height = 0 
            else:
                left_height = node._left._height
                
            if node._right is None: 
                right_height = 0   
            else: 
                right_height = node._right._height
            
            
            if node._height == 1 + max(left_height, right_height):
                valid = True
                if node._left is not None:
                    valid = valid and self._max_r_aux(node._left)._value < node._value
                
                if node._right is not None:
                    valid = valid and self._min_r_aux(node._right)._value > node._value
            else:
                valid = False
        else:
            valid = True
            
        return valid 


    def update(self, value, update):
        """
        ---------------------------------------------------------
        Updates a value in a bst by applying a functions to it.
        Use: bst.update(value, func)
        ---------------------------------------------------------
        Parameters:
            value - a comparable part of a data element (?)
            update - an update functions compatible with value (functions)
        Returns:
            updated - True if value is in bst and is updated, False if
            value is not in bst, but adds value to bst in that case.
            (Iterative algorithm.)
        --------------------------------------------------------- -
        """

        # your code here


    def update_r(self, key, update):
        """
        ---------------------------------------------------------
        Updates a value in a bst by applying a functions to it.
        Use: bst.update(value, func)
        ---------------------------------------------------------
        Parameters:
            value - a comparable part of a data element (?)
            update - an update functions compatible with value (functions)
        Returns:
            updated - True if value is in bst and is updated, False if
            value is not in bst, but adds value to bst in that case.
            (Recursive algorithm.)
        --------------------------------------------------------- -
        """

        # your code here


    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        node = self._root
        a = []
        self._inorder_aux(node, a)
        
        return a
            
    def _inorder_aux(self, node, inorder):
        if node is not None:
            self._inorder_aux(node._left, inorder)    
            inorder.append(deepcopy(node._value))
            self._inorder_aux(node._right, inorder)
        
        return inorder


    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        node = self._root
        a = []
        self._preorder_aux(node, a)
        
        return a
            
    def _preorder_aux(self, node, preorder):
        if node is not None:
            preorder.append(deepcopy(node._value))
            self._preorder_aux(node._left, preorder)    
            self._preorder_aux(node._right, preorder)
        
        return preorder
            
    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        node = self._root
        a = []
        self._postorder_aux(node, a)
        
        return a
            
    def _postorder_aux(self, node, postorder):
        if node is not None:
            self._postorder_aux(node._left, postorder)    
            self._postorder_aux(node._right, postorder)
            postorder.append(deepcopy(node._value))
        
        return postorder    
        
    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        values = []
        node = self._root
        
        if node is not None:
            
            temp = []
            temp.append(node)
            
            while len(temp) != 0:
                temp2 = []
                
                for i_node in temp:
                    values.append(i_node._value)
                                            
                    if i_node._left is not None:
                        temp2.append(i_node._left)
                    if i_node._right is not None:
                        temp2.append(i_node._right)
                    
                temp = temp2
                
        return values
        

    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """

        # your code here


    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
