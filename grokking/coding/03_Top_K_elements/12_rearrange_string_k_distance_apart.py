#
'''
Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’ distance apart from each other.

Example 1:

Input: "mmpp", K=2
Output: "mpmp" or "pmpm"
Explanation: All same characters are 2 distance apart.
Example 2:

Input: "Programming", K=3
Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more  
Explanation: All same characters are 3 distance apart.
Example 3:

Input: "aab", K=2
Output: "aba"
Explanation: All same characters are 2 distance apart.
Example 4:

Input: "aappa", K=3
Output: ""
Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.
'''

#########################################################################################################
# maxheap
# TC: O(N log N)
# SC: O(N)

from heapq import *
from collections import deque

def reorganize_string(word, k):
  if k <= 1:
    return word
  
  freqmap = {}
  for c in word:
    freqmap[c] = freqmap.get(c, 0) + 1
   
  maxheap = []
  for c, freq in freqmap.items():
    heappush(maxheap, (-freq, c))
    
  output = []
  q = deque()
  while maxheap:
    freq, c = heappop(maxheap)
    output.append(c)
    
    # decrement the freq and add to queue
    q.append((c, freq + 1))
    if len(q) == k:
      char, f = q.popleft()
      if -f > 0:
        heappush(maxheap, (f, char))
        
  return "".join(output) if len(output) == len(word) else ""

'''
Output
1.07s
Reorganized string: mpmp
Reorganized string: gmrPagimnor
Reorganized string: aba
Reorganized string: 
'''
        
