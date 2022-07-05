# https://leetcode.com/problems/3sum/
'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

###############################################################################################################################
# Brute force : TLE
# TC: O(n^3)
# SC: O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                        output.add(tuple(sorted([nums[i], nums[j] , nums[k]])))
        return output
      
###############################################################################################################################
# HASHSET
# TC: O(n^2)
# SC: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        dups = set()
        seen = {}
        
        for i, n1 in enumerate(nums):
            if n1 not in dups:
                dups.add(n1)
                for j, n2 in enumerate(nums[i+1:]):
                    complement = -n1 - n2
                    if complement in seen and seen[complement] == i:
                        curr = tuple(sorted([n1, n2, complement]))
                        output.add(curr)
                    seen[n2] = i
        return output
