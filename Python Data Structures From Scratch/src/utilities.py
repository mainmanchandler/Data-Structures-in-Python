"""
------------------------------------------------------------------------
Utility functions1.
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-21"
------------------------------------------------------------------------
"""
#imports
from Stack_array import Stack

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while len(source) != 0:
        value = source.pop(-1)
        stack.push(value)
            
    return None


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not stack.is_empty():
        target.insert(0, stack.pop())
    
    return None
    

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()
    print('Empty stack: ')
    print('Is_Empty: {}'.format(s.is_empty()))
    
    for i in source:
        s.push(i)
    
    print('\nFull stack: ')
    print('Is_Empty: {}\n'.format(s.is_empty()))
    print('Pop: {}'.format(s.pop()))
    print('\nPeek: {}'.format(s.peek()))
    
    return None




#--------------------------------------------------------------------------------------------------------------------------------

#imports
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while len(source) != 0:
        
        value = source.pop(0)
        queue.insert(value)
        
    return None


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())
    
    return None
    
  

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) != 0:
        value = source.pop(0)
        pq.insert(value)
    
    
    return None


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not pq.is_empty():
        target.append(pq.remove())
    
    return None



def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    
    q = Queue()
    print('Empty queue: ')
    print('Is_Empty: {}\n\n'.format(q.is_empty()))
    
    #fill with values from list "a"
    for i in a:
        q.insert(i)
        
    print('Active Queue:')
    print('Is_Empty: {}\n\n'.format(q.is_empty()))
    
    #peek the first value to be removed
    print("--Peek at first in line (list):-- \n{}\n".format(q.peek()))
    
    #remove the first value entered in the queue
    q.remove()
    print('Removed first, as first come - first server order\n')
    
    #peek the next value to be removed
    print("--Peek at next in line (list) #2:-- \n{}".format(q.peek()))

    return None
    
    
    
def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    
    print('Empty priority queue: ')
    print('Is_Empty: {}\n\n'.format(pq.is_empty()))
    
    #fill with values from list "a"
    for i in a:
        pq.insert(i)
        
    print('Active priority queue:')
    print('Is_Empty: {}\n\n'.format(pq.is_empty()))
    
    print("--Peek at first Priority:-- \n{}\n".format(pq.peek()))
    
    #removal of first priority
    first = pq.remove()
    
    #Verify if the removal and peek for next value of priority
    print('--item removed:-- \n{}\n\n--Next:-- \n{}'.format(first, pq.peek()))

    return None





#--------------------------------------------------------------------------------------------------------------------------------

#imports
from List_array import List
from Food import Food

def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contents of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    while len(source) != 0:
        value = source.pop(0)
        llist.insert(i, value)
        i += 1
        
    return None
    


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    i = 0
    while len(llist) != 0:
        value = llist.pop(0)
        target.insert(i, value)
        i += 1
    
    return None
    


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
        
    print('Empty List: ')
    print('Is_Empty: {}\n\n'.format(lst.is_empty()))
    
    #fill with values from list "a"
    for i in source:
        lst.append(i)
        
    print('Filled List:')
    print('Is_Empty: {}\n\n'.format(lst.is_empty()))
        
    inserter = source[2]
    lst.insert(5, inserter)
    key = Food('Moo Goo Guy Pan', 1, None, None)
    print("--Remove value in List:-- \n{}\n".format(lst.remove(key)))
    
    print("--Count of how many similar keys in the list:-- \n{}\n".format(lst.count(key))) # I duplicated the key for valid varification
    
    print("--Append food object to the end of the list:-- \n{}\n".format(lst.append(key)))
    
    print("--Count of how many similar keys in list #2 (to varify append):-- \n{}\n".format(lst.count(key))) 
        
    print("--Find index of a food object in the list:-- \n{}\n".format(lst.index(key))) 
    #remember the index is not going to be 0 as we removed the occurrence in the list
    
    print("--Find the first occurrence of the object in the list:-- \n{}\n".format(lst.find(key)))
    
    print("--Find the max value in the list:-- \n{}\n".format(lst.max()))
    print("--Find the min value in the list:-- \n{}\n".format(lst.min()))


    return None






#--------------------------------------------------------------------------------------------------------------------------------

