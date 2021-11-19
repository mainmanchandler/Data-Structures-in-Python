"""
------------------------------------------------------------------------
Assignment 4 - functions file
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-27"
------------------------------------------------------------------------
"""
#imports
from Priority_Queue_array import Priority_Queue
from copy import deepcopy

def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
            
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    while not source.is_empty():
        check = source.remove()
        
        if check < key:
            target1.insert(check)
        elif check >= key:
            target2.insert(check)
    
    
    return target1, target2
    
    
def pq_split_alt(source):
    """
    -------------------------------------------------------
    Splits a priority queue into two with values going to alternating
    priority queues. The source priority queue is empty when the method
    ends. The order of the values in source is preserved.
    Use: target1, target2 = pq_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        
    Returns:
        target1 - a priority queue that contains alternating values
            from source (Priority_Queue)
            
        target2 - priority queue that contains  alternating values
            from source (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    altn = True
    
    while not source.is_empty():
        value = source.remove()
        
        if altn:
            target1.insert(value)
        else:
            target2.insert(value)
        altn = not altn
   
    return target1, target2
  
    

def prims(graph, start_node):
    """
    -------------------------------------------------------
    Applies Prim's Algorithm to a graph.
    Use: edges, total = prims(graph, node)
    -------------------------------------------------------
    Parameters:
        graph - graph to evaluate (Graph)
        start_node - name of node to start evaluation from (str)
    Returns:
        edges - the list of the edges traversed (list of Edge) #ask brown if he wants them as string or objects when returned
        total - total distance of all edges traversed (int)
    -------------------------------------------------------
    """
    
    pq = Priority_Queue() #priority queue to output the highest priority
    edges = [] #the cheapest and already visited edges
    
    visited_nodes = [] #adds the opposite end of that edge to list
    visited_nodes.append(start_node)
    
    all_nodes = graph.node_names() #all nodes in graph
    total = 0 #total cost
    
    node_up_next = start_node

    while all_nodes != visited_nodes:
        
        for edge in graph.edges_by_node(node_up_next):
            pq.insert(edge)

        sequent_edge = pq.remove()
        
        while sequent_edge.end() in visited_nodes and not pq.is_empty():
            sequent_edge = pq.remove()
        
        
        visited_nodes.append(sequent_edge.end())
        visited_nodes.sort() #to ensure the while comparison is met
        
        edges.append(sequent_edge)
        
        total += sequent_edge.distance #add up total
    
        node_up_next = sequent_edge.end()
    
    return edges, total
    
    
    
    
    
    
