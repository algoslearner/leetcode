#
'''
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
'''

###########################################################################################################
# sliding window
# TC: O(N)
# SC: O(1)

def length_of_longest_substring(arr, k):
  maxlength = 0
  start = 0
  freqmap = {}
  
  for end in range(len(arr)):
    right_char = arr[end]
    freqmap[right_char] = freqmap.get(right_char, 0) + 1
    
    window_size = end - start + 1
    if window_size - freqmap[1] > k:
      left_char = arr[start]
      if left_char == 1:
        freqmap[1] -= 1
      start ++ 1
    
    maxlength = max(maxlength, end - start + 1)
  return maxlength
