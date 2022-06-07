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

###########################################################################################################
# BRUTE FORCE : TLE
# TC: O(n3), SC: O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                        output.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                        
        return output
      
      
      
###########################################################################################################
# HASHSET
# TC: O(n2)
# SC: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        dups = set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        output.add(tuple(sorted([val1, val2, complement])))
                    seen[val2] = i
        return output

###########################################################################################################
# Two Pointer
# TC: O(n2 + nlogn)
# SC: O(log n) or O(n) for sorting

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, output)
                
        return output
    
    def twoSum(self, nums: List[int], i: int, output: List[List[int]]):
        lo = i + 1
        hi = len(nums) - 1
        while lo < hi:
            triplet = nums[i] + nums[lo] + nums[hi]
            if triplet < 0:
                lo += 1
            elif triplet > 0:
                hi -= 1
            else:
                output.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                
                # avoid duplicates
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                
                        
