# 
'''
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

Example 1:

Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0
    3   
    2   
    0   
    1   
Example 2:

Input: Vertices=5, Edges=[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
Output: Following are all valid topological sorts for the given graph:
1) 4, 2, 3, 0, 1
2) 4, 3, 2, 0, 1
3) 4, 3, 2, 1, 0
4) 4, 2, 3, 1, 0
5) 4, 2, 0, 3, 1
    4   
    2   
    3   
    0   
    1   
Example 3:

Input: Vertices=7, Edges=[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]
Output: Following are all valid topological sorts for the given graph:
1) 5, 6, 3, 4, 0, 1, 2
2) 6, 5, 3, 4, 0, 1, 2
3) 5, 6, 4, 3, 0, 2, 1
4) 6, 5, 4, 3, 0, 1, 2
5) 5, 6, 3, 4, 0, 2, 1
6) 5, 6, 3, 4, 1, 2, 0

There are other valid topological ordering of the graph too.
'''

###########################################################################################################
# TC: O(V + E)
# SC: O(V + E)

from collections import deque

def topological_sort(vertices, edges):
  sortedOrder = []
  
  if vertices <= 0: return sortedOrder
  
  # initialize graph
  indegree = {i : 0 for i in range(vertices)}
  adj_list_graph = {i : [] for i in range(vertices)}

  # build graph
  for edge in edges:
        parent, child = edge[0], edge[1]
        adj_list_graph[parent].append(child)
        indegree[child] += 1

  # find all sources: vertices with zero indegree
  sources = deque()
  for key in indegree:
        if indegree[key] == 0:
              sources.append(key)

  # for each source, populate sortedorder
  while sources:
        source = sources.popleft()
        sortedOrder.append(source)
        for child in adj_list_graph[source]:
              indegree[child] -= 1
              if indegree[child] == 0: sources.append(child)

  # check if any cycle
  if len(sortedOrder) != vertices:
        return []

  return sortedOrder


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
