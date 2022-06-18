#
'''
Given a string, sort it based on the decreasing frequency of its characters.

Example 1:

Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.
Example 2:

Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
'''

###################################################################################################################
# maxheap
# TC: O(N log N)
# SC: O(N)

from heapq import *

def sort_character_by_frequency(word):
  freqmap = {}
  for c in word:
    freqmap[c] = freqmap.get(c, 0) + 1
  
  maxheap = []
  for c, freq in freqmap.items():
    heappush(maxheap, (-freq, c))
  
  # output
  output = []
  while maxheap:
    freq, c = heappop(maxheap)
    for _ in range(-freq):
      output.append(c)
  return ''.join(output)


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()
