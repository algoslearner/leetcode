# 3sum
'''
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
'''

#############################################################################################################################
# two pointers
# TC: O(N^2)
# SC: O(N)

def triplet_sum_close_to_target(arr, target_sum):
  min_target_diff = float('inf')
  closest_sum = 0
  arr.sort()

  for i in range(len(arr)):
    left = i+1
    right = len(arr) - 1
    while left < right:
      triplet_sum = arr[i] + arr[left] + arr[right]
      target_diff = target_sum - triplet_sum

      if abs(target_diff) < abs(min_target_diff):
        min_target_diff = target_diff
        closest_sum = triplet_sum
      
      if target_diff > 0:
        left += 1
      else:
        right -= 1

  return closest_sum
