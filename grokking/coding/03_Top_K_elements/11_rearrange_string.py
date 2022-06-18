#
'''
Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

Example 1:

Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each other.
Example 2:

Input: "Programming"
Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
Explanation: None of the repeating characters come next to each other.
Example 3:

Input: "aapa"
Output: ""
Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".
'''

####################################################################################################################
# maxheap
# TC; O(N log N), where N is the number of characters in the input string
# SC: O(N)

from heapq import *


def rearrange_string(word):
  freqmap = {}
  for c in word:
    freqmap[c] = freqmap.get(c, 0) + 1
  
  maxheap = []
  for c, freq in freqmap.items():
    heappush(maxheap, (-freq, c))
  
  prev_c = None
  prev_freq = 0
  output = []
  while maxheap:
    freq, c = heappop(maxheap)
    if prev_c and -prev_freq > 0:
      heappush(maxheap, (prev_freq, prev_c))
    
    output.append(c)
    prev_c = c
    prev_freq = freq + 1 # decrement freq by 1
  
  return ''.join(output) if len(output) == len(word) else ""

def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))


main()

'''
Output
0.88s
Rearranged string:  papap
Rearranged string:  gmrPagimnor
Rearranged string:  
'''
