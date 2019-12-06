#!/usr/bin/env python

import time
import string
import collections
start_time = time.time()

# A Python program to print topological sorting of a graph 
# using indegrees 
from collections import defaultdict 

#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 


    # The function to do Topological Sort. 
    def topologicalSort(self): 
        
        # Create a vector to store indegrees of all 
        # vertices. Initialize all indegrees as 0. 
        in_degree = [0]*(self.V) 
        
        # Traverse adjacency lists to fill indegrees of 
        # vertices. This step takes O(V+E) time 
        for i in self.graph: 
            for j in self.graph[i]: 
                in_degree[j] += 1

        # Create an queue and enqueue all vertices with 
        # indegree 0 
        queue = [] 
        for i in range(self.V): 
            if in_degree[i] == 0: 
                queue.append(i) 

        #Initialize count of visited vertices 
        cnt = 0

        # Create a vector to store result (A topological 
        # ordering of the vertices) 
        top_order = [] 

        # One by one dequeue vertices from queue and enqueue 
        # adjacents if indegree of adjacent becomes 0 
        while queue: 

            # Extract front of queue (or perform dequeue) 
            # and add it to topological order 
            u = queue.pop(0) 
            top_order.append(u) 

            # Iterate through all neighbouring nodes 
            # of dequeued node u and decrease their in-degree 
            # by 1 
            for i in self.graph[u]: 
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue 
                if in_degree[i] == 0: 
                    queue.append(i) 

            cnt += 1

        # Check if there was a cycle 
        if cnt != self.V: 
            print "There exists a cycle in the graph"
        else : 
            #Print topological order 
            print top_order 
            return top_order
            
def getLHS(step):
    return step[step.find("Step")+4:step.find("must")].strip()
    
def getRHS(step):
    return step[step.find("step")+4:step.find("can")].strip()
    
def findUniqueSteps(steps):
    elemList = []
    for step in steps:
        lhs = getLHS(step)
        rhs = getRHS(step)
        elemList.append(lhs)
        elemList.append(rhs)
        
    return sorted(list(set(elemList)))

with open("input2.txt") as f:
    steps = f.read().splitlines()

    g=Graph(len(findUniqueSteps(steps)))
    for step in steps:
        lhs = getLHS(step)
        rhs = getRHS(step)
        #print(lhs)
        #print(rhs)
        g.addEdge(ord(lhs)-65, ord(rhs)-65)
        
    print "Following is a Topological Sort of the given graph"
    ll = g.topologicalSort()
    stringList = []
    for l in ll:
        stringList.append(chr(l+65))
    print(''.join(stringList))
    
print("--- %s seconds ---" % (time.time() - start_time))