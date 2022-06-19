#
'''
You are given a list of tasks that need to be run, in any order, on a server. 
Each task will take one CPU interval to execute but once a task has finished, 
it has a cooling period during which it can’t be run again. 

If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.

If at any time the server can’t execute any task then it must stay idle.

Example 1:

Input: [a, a, a, b, c, c], K=2
Output: 7
Explanation: a -> c -> b -> a -> c -> idle -> a
Example 2:

Input: [a, b, a], K=3
Output: 5
Explanation: a -> b -> idle -> idle -> a
'''

##################################################################################################################
# maxheap
# TC: O(N log N)
# SC: O(N)

from heapq import *

def schedule_tasks(tasks, k):
  intervals = 0
  
  freqmap = {}
  for t in tasks:
    freqmap[t] = freqmap.get(t, 0) + 1
  
  maxheap = []
  for t, freq in freqmap.items():
    heappush(maxheap, (-freq, t))
    
  while maxheap:
    waitlist = []
    
    # try to execute as many as 'k+1' tasks from the max-heap
    n = k + 1
    while n > 0 and maxheap:
      intervals += 1
      freq, t = heappop(maxheap)
      if -freq > 1:
        # decrement the frequency and add to the waitList
        waitlist.append((freq + 1, t))
      n -= 1
      
    # put all the waiting list back on heap
    for freq, char in waitlist:
      heappush(maxheap, (freq, char))
      
    if maxheap:
      intervals += n
      
  return intervals
        
