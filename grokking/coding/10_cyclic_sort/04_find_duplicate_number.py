# https://leetcode.com/problems/find-the-duplicate-number/
'''
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
The array has only one duplicate but it can be repeated multiple times. 

Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:

Input: [2, 1, 3, 3, 5, 4]
Output: 3
Example 3:

Input: [2, 4, 1, 4, 4]
Output: 4
'''

########################################################################################################################
# sort
# TC: O(n log n)
# SC: O(1)

def find_duplicate(nums):
  nums.sort()
  for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
      return nums[i]
  return -1

########################################################################################################################
# set
# TC: O(n)
# SC: O(n)

def find_duplicate(nums):
  seen = set()
  for n in nums:
    if n in seen:
      return n
  return -1

########################################################################################################################
# Floyd's hare and tortoise algorithm
# TC: O(n)
# SC: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # find entrance to cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
 
########################################################################################################################
# cyclic sort
# TC: O(n)
# SC: O(1)

def find_duplicate(nums):
  i = 0
  while i < len(nums):
    if nums[i] != i + 1:
      j = nums[i] - 1
      if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]  # swap
      else:  # we have found the duplicate
        return nums[i]
    else:
      i += 1

  return -1
