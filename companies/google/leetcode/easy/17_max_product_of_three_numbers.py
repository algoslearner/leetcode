# https://leetcode.com/problems/maximum-product-of-three-numbers/
'''
628. Maximum Product of Three Numbers

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
 

Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
'''

#######################################################################################################
# SORT
# TC: O(N log N)
# SC: O(log N)

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[len(nums)-1],
                  nums[len(nums)-1] * nums[len(nums)-2] * nums[len(nums)-3])
      
#######################################################################################################
# HEAP
# TC: O(N log N)
# SC: O(log N)

import heapq
class Solution:
    def maximumProduct(self, array):
        largest = heapq.nlargest(3, array)
        smallest = heapq.nsmallest(2,array)

        return max(largest[0] * largest[1] * largest[2], largest[0] * smallest[0] * smallest[1] )
      
#######################################################################################################
# single scan
# TC: O(N)
# SC: O(1)

import bisect

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        total, negative = [], [] # Space O(3)      
        for num in nums:
            bisect.insort(total, num) # O(3)
            if len(total) > 3:
                total.pop(0)
            if num < 0:
                bisect.insort(negative, abs(num)) # O(2)
                if len(negative) > 2:
                    negative.pop(0)                
        # Candidate by multiplying max 3 nums
        res = total[-3] * total[-2] * total[-1]
        if len(negative) < 2:
            return res
        else:
            return max(res, total[-1] * negative[-2] * negative[-1])
