'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''

###########################################################################################################
# READ: https://leetcode.com/problems/subsets/solution/
# METHOD-1: CASCADING
# BRUTE FORCE: TC, SC: Exponential
  
  class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        
        return output
      
      
#######################################################################################################
# METHOD -2 : Back tracking
# TC: Exponential
# SC: O(N)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
                return
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
      
      
      
###################################################################################################
# BACKTRACKING

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backTrack(start, cur_list):
            ans.append(cur_list[:])
            
            for j in range(start, n):
                cur_list.append(nums[j])
                backTrack(j+1, cur_list)
                cur_list.pop()
                
        n = len(nums)
        ans = []
        backTrack(0, [])
        return ans
