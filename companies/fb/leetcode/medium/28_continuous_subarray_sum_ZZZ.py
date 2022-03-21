'''
Given an integer array nums and an integer k, 
return true if nums has a continuous subarray of size at least two 
whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
'''

# https://leetcode.com/problems/continuous-subarray-sum/discuss/338417/Python-Solution-with-explanation
# Same as Subarray sum equals K with modification. 
# Basic idea is that, If you get the same remainder again, it means that you've encountered some sum which is a multiple of K.

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # Keep track of the prefix sum remainder
        prefix_sum = 0
        
        # Dictionary of prefix sums and their indices(0 is seen before the array)
        prefix_sum_indices = {0: -1}
        
        for index, num in enumerate(nums):
            # Compute the remainder when dividing the new sum by k
            prefix_sum = (prefix_sum + num) % k
            
            # Check if this remainder has been encountered before and of length 2
            if prefix_sum in prefix_sum_indices and index - prefix_sum_indices[prefix_sum] > 1:
                return True
            
            # Add this index if it is hasn't been encountered before
            if prefix_sum not in prefix_sum_indices:
                prefix_sum_indices[prefix_sum] = index
        
        return False
        
 # Time : O(n)
# Space: O(min(n,k))
