__author__ = 'fernote7'

from sys import maxint
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import time

grafo = {'a': {'b': 1, 'e': 4, 'f': 8},
         'b': {'c': 2, 'f': 6, 'g': 6},
         'c': {'d': 1, 'g': 2},
         'd': {'g': 1, 'h': 4},
         'e': {'f': 5},
         'g': {'f': 1, 'h': 1},
         'h': {'f': 1, 'e': 5}}


start_time = time.time()

def dijkstra(grafo,start,end,visited=[],distance={},predecessors={}):
    """Find the shortest path between start and end nodes in a grafo"""

    # detect if it's the first time through, set current distance to zero
    if not visited: distance[start]=0
    # process vizinhos as per algorithm, keep track of predecessors
    for vizinho in grafo[start]:
        if vizinho not in visited:
            dist_vizinho = distance.get(vizinho,maxint)
            tentativedist = distance[start] + grafo[start][vizinho]
            if tentativedist < dist_vizinho:
                distance[vizinho] = tentativedist
                predecessors[vizinho]=start
    # vizinhos processed, now mark the current node as visited
    visited.append(start)
    # finds the closest nonvisited node to the start
    nonvisited = dict((k, distance.get(k,maxint)) for k in grafo if k not in visited)
    try:
        closestnode = min(nonvisited, key=nonvisited.get)
    except:
        pass

    # we've found our end node, now find the path to it, and return
    if start==end:
        return distance[start]
    # now we can take the closest node and recurse, making it current


    return dijkstra(grafo,closestnode,end,visited,distance,predecessors)

print "Time elapsed: ", time.time() - start_time, "s"
print dijkstra(grafo,'a','h')



'''
grafo = {'a': {'w': 14, 'x': 7, 'y': 9},
         'b': {'w': 9, 'z': 6},
         'w': {'a': 14, 'b': 9, 'y': 2},
         'x': {'a': 7, 'y': 10, 'z': 15},
         'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
         'z': {'b': 6, 'x': 15, 'y': 11}}
'''





start_time = time.time()
G = nx.DiGraph()
G.add_edge('a', 'b', distance=1)
G.add_edge('a', 'e', distance=4)
G.add_edge('a', 'f', distance=8)
G.add_edge('b', 'c', distance=2)
G.add_edge('b', 'f', distance=6)
G.add_edge('b', 'g', distance=6)
G.add_edge('c', 'd', distance=1)
G.add_edge('c', 'g', distance=2)
G.add_edge('d', 'g', distance=1)
G.add_edge('d', 'h', distance=4)
G.add_edge('e', 'f', distance=5)
G.add_edge('g', 'f', distance=1)
G.add_edge('g', 'h', distance=1)
print "Time elapsed: ", time.time() - start_time, "s"


print(nx.dijkstra_path_length(G, 'a', 'h', 'distance'))



nx.draw_networkx(G, arrows=True)
#plt.axis('off')
#plt.show()

