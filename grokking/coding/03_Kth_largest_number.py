#
'''
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
'''

###########################################################################################################################
# minheap
# TC: O(N log k)
# SC: O(k)

from heapq import *

def find_k_largest_numbers(nums, k):
  minheap = []

  for i in range(k):
    heappush(minheap, nums[i])
  
  # top of minheap is the smallest number in heap
  for i in range(k, len(nums)):
    if nums[i] > minheap[0]:
      heappop(minheap)
      heappush(minheap, nums[i])
  
  return minheap

def main():
  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()

