#
'''
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. 
Each task can have some prerequisite tasks which need to be completed before it can be scheduled. 
Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: There is only possible ordering of the tasks.
Example 2:

Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
Output: 
1) [3, 2, 0, 1]
2) [3, 2, 1, 0]
Explanation: There are two possible orderings of the tasks meeting all prerequisites.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: 
1) [0, 1, 4, 3, 2, 5]
2) [0, 1, 3, 4, 2, 5]
3) [0, 1, 3, 2, 4, 5]
4) [0, 1, 3, 2, 5, 4]
5) [1, 0, 3, 4, 2, 5]
6) [1, 0, 3, 2, 4, 5]
7) [1, 0, 3, 2, 5, 4]
8) [1, 0, 4, 3, 2, 5]
9) [1, 3, 0, 2, 4, 5]
10) [1, 3, 0, 2, 5, 4]
11) [1, 3, 0, 4, 2, 5]
12) [1, 3, 2, 0, 5, 4]
13) [1, 3, 2, 0, 4, 5]
'''

#################################################################################################
# TC: O(V! + E)
# SC: O(V! + E)

from collections import deque

def print_orders(tasks, prerequisites):
  sortedOrder = []
  if tasks <= 0: return []

  # initialize the graph
  indegree = {i : 0 for i in range(tasks)}
  adj_list_graph = {i : [] for i in range(tasks)}

  # build graph
  for prereq in prerequisites:
    parent, child = prereq[0], prereq[1]
    adj_list_graph[parent].append(child)
    indegree[child] += 1
  
  # find sources
  sources = deque()
  for key in indegree:
    if indegree[key] == 0:
      sources.append(key)
  
  # print all order
  print_all_orders(adj_list_graph, indegree, sources, sortedOrder)

def print_all_orders(adj_list_graph, indegree, sources, sortedOrder):
  if sources:
    for source in sources:
      sortedOrder.append(source)
      sourcesForNextCall = deque(sources)
      sourcesForNextCall.remove(source)

      for child in adj_list_graph[source]:
        indegree[child] -= 1
        if indegree[child] == 0: sourcesForNextCall.append(child)
      
      # recursive call to print other orders
      print_all_orders(adj_list_graph, indegree, sourcesForNextCall, sortedOrder)
      
      # backtrack
      sortedOrder.remove(source)
      for child in adj_list_graph[source]:
        indegree[child] += 1
      
  # print
  if len(sortedOrder) == len(indegree):
    print(sortedOrder)



def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()

'''
Output
1.23s
Task Orders: 
[0, 1, 2]
Task Orders: 
[3, 2, 0, 1]
[3, 2, 1, 0]
Task Orders: 
[0, 1, 4, 3, 2, 5]
[0, 1, 3, 4, 2, 5]
[0, 1, 3, 2, 4, 5]
[0, 1, 3, 2, 5, 4]
[1, 0, 3, 4, 2, 5]
[1, 0, 3, 2, 4, 5]
[1, 0, 3, 2, 5, 4]
[1, 0, 4, 3, 2, 5]
[1, 3, 0, 2, 4, 5]
[1, 3, 0, 2, 5, 4]
[1, 3, 0, 4, 2, 5]
[1, 3, 2, 0, 5, 4]
[1, 3, 2, 0, 4, 5]
'''

