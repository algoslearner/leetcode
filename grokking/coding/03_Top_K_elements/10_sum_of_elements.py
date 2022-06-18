#
'''
Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

Example 1:

Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
Output: 23
Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
between 5 and 15 is 23 (11+12).
Example 2:

Input: [3, 5, 8, 7], and K1=1, K2=4
Output: 12
Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest 
number (8) is 12 (5+7).

'''

####################################################################################################
# brute force, sorting
# tc: O(n log n)
# sc: O(1)

def find_sum_of_elements(nums, k1, k2):
  nums.sort()
  if len(nums) < k1 or len(nums) < k2:
    return 0

  sumSub = 0
  for i in range(len(nums)):
    if i+1 > k1 and i+1 < k2:
      sumSub += nums[i]
  return sumSub

####################################################################################################
# heap
# tc: O(n log nk)
# sc: O(k)

from heapq import *


def find_sum_of_elements(nums, k1, k2):
  minHeap = []
  # insert all numbers to the min heap
  for num in nums:
    heappush(minHeap, num)

  # remove k1 small numbers from the min heap
  for _ in range(k1):
    heappop(minHeap)

  elementSum = 0
  # sum next k2-k1-1 numbers
  for _ in range(k2 - k1 - 1):
    elementSum += heappop(minHeap)

  return elementSum
