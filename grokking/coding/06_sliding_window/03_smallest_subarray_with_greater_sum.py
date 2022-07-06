#
'''
Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0 if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].

Example 2:

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [8].

Example 3:

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to ‘8’ are [3, 4, 1] or [1, 1, 6].
'''

#######################################################################################################################################################
# sliding window
# TC: O(n)
# SC: O(1)

def smallest_subarray(arr, s):
  start = 0
  sub_sum = 0.0
  min_diff = float('inf')
  
  for end in range(len(arr)):
    sub_sum += arr[i]
    if sub_sum >= s:
      min_diff = min(min_diff, sub_sum)
      sub_sum -= arr[start]
      start += 1
      
  if min_diff == float('inf'): return 0
  return min_diff
