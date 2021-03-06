# 
'''
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. 
Each task can have some prerequisite tasks which need to be completed before it can be scheduled. 
Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs
to finish before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2] 
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: []
Explanation: The tasks have a cyclic dependency, therefore they cannot be scheduled.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: [0 1 4 3 2 5] 
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5] 
'''

########################################################################################################################################
# tc: O(V + E)
# sc: O(V + E)

from collections import deque

def find_order(tasks, prerequisites):
  sortedOrder = []
  if tasks <= 0:
    return []

  # initialize graph
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

  # for each source, populate sortedOrder
  while sources:
    source = sources.popleft()
    sortedOrder.append(source)
    for child in adj_list_graph[source]:
      indegree[child] -= 1
      if indegree[child] == 0: sources.append(child)

  # if any cycle
  if len(sortedOrder) != tasks: return []


  return sortedOrder


def main():
  print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
