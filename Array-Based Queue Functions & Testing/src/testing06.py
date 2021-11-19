"""
------------------------------------------------------------------------
prim function testing
------------------------------------------------------------------------
Author:  Chandler Mayberry
Last_updated = "2020-01-27"
------------------------------------------------------------------------
"""
#imports
from functions import prims
from Graph import Edge, Graph, graph_test

start_node = 'A'
#start_node = 'B'
#start_node = 'C'
#start_node = 'G'

data = (
    (['A', 'B'], 2), (['A', 'C'], 3), (['A', 'D'], 7), (['B', 'C'], 6),
    (['B', 'G'], 4), (['C', 'E'], 1), (['C', 'F'], 8), (['D', 'E'], 5),
    (['E', 'F'], 4), (['F', 'G'], 2)
    )
'''
data = (
    (['A', 'B'], 3), (['A', 'C'], 3), (['B', 'H'], 6), (['B', 'C'], 3),
    (['H', 'I'], 4), (['I', 'H'], 4), (['B', 'A'], 3), (['C', 'B'], 3),
    (['C', 'D'], 2), (['H', 'F'], 3), (['E', 'F'], 7), (['F', 'E'], 7), 
    (['F', 'G'], 5), (['G', 'D'], 7),(['D', 'G'], 7), (['D', 'E'], 8), (['D', 'C'], 2)
    )
'''    

graph_test(data)

#THIS TRANSFERS THE DATA INTO A GRAPH
edges = []
for d in data:
    edge = Edge(d[0], d[1])
    edges.append(edge)
# Initialize the graph.
graph = Graph(edges)



edges, total = prims(graph, start_node)
print('--List of edge objects traversed:--\n')
for i in edges:
    print(i)
print('\n--Total of edges traversed:--\n {}'.format(total))




