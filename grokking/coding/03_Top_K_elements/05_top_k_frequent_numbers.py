#
'''
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.
'''

##############################################################################################################
# minheap
# TC: O(N + N log k)
# SC: O(N)

from heapq import *

def find_k_frequent_numbers(nums, k):
  freqmap = {}
  for num in nums:
    freqmap[num] = freqmap.get(num, 0) + 1
  
  minheap = []
  for num, freq in freqmap.items():
    heappush(minheap, (freq, num))
    if len(minheap) > k:
      heappop(minheap)

  # convert heap to list
  topnumbers = []
  while minheap:
    topnumbers.append(heappop(minheap)[1])
  return topnumbers


def main():
  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()

