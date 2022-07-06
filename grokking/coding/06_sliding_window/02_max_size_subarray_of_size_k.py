#
'''
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

#####################################################################################################################################
# brute force
# TC: O(nk)
# SC: O(1)

def max_subarray_sum(arr, k) -> int:
  maxsum = 0
  currsum = 0
  
  for i in range(len(arr)):
    currsum = 0
    for j in range(i, i+k):
      currsum += arr[j]
    maxsum = max(maxsum, currsum)
    
  return maxsum

#####################################################################################################################################
# sliding window
# TC: O(n)
# SC: O(1)

def max_subarray_sum(arr, k) -> int:
  maxsum = 0
  currsum = 0
  start = 0
  
  for end in range(len(arr)):
    currsum += arr[end]
    if end >= k - 1:
      maxsum = max(maxsum, currsum)
      currsum -= arr[start]
      start += 1
      
  return maxsum
