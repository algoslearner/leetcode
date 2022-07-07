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

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlength = 0
        start = 0
        max_ones_count = 0
        
        for end in range(len(nums)):
            right_char = nums[end]
            if right_char == 1:
                max_ones_count += 1
            
            window_size = end - start + 1
            if window_size - max_ones_count > k:
                left_char = nums[start]
                if left_char == 1:
                    max_ones_count -= 1
                start += 1
            
            maxlength = max(maxlength, end - start + 1)
        return maxlength
            
