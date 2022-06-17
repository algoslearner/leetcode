# 
'''
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. 
Each task can have some prerequisite tasks which need to be completed before it can be scheduled. 
Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs 
to finish before '2' can be scheduled. One possible scheduling of tasks is: [0, 1, 2] 
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have a cyclic dependency, therefore they cannot be scheduled.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]
'''

###################################################################################################################
# TC: O(V + E)
# SC: O(V + E)

from collections import deque

def is_scheduling_possible(tasks, prerequisites):
  sortedOrder = []
  if tasks <= 0:
        return False

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

  # check for any cycle
  return len(sortedOrder) == tasks


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))

main()

'''
Output
0.84s
Is scheduling possible: True
Is scheduling possible: False
Is scheduling possible: True
'''
