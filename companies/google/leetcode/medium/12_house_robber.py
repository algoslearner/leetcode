# https://leetcode.com/problems/house-robber/
'''
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
'''

###########################################################################################
# RECURSION
# TC: O(n)
# SC: O(n)

class Solution:
    def __init__(self):
        self.memo = {}
        
    def robFrom(self, i, nums):
        # no more houses left to examine
        if i >= len(nums):
            return 0
        
        if i in self.memo:
            return self.memo[i]
        
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
        self.memo[i] = ans
        return ans
        
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.robFrom(0, nums)

###########################################################################################
# DP
# TC: O(n)
# SC: O(n)

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        # Special handling for empty case.
        if not nums:
            return 0
        
        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)
        
        # Base case initialization.
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]
        
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            
            # Same as recursive solution.
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
            
        return maxRobbedAmount[0]    
      
###########################################################################################
# DP optimized
# TC: O(n)
# SC: O(1)

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        
        # Special handling for empty case.
        if not nums:
            return 0
        
        N = len(nums)
        
        rob_next_plus_one = 0
        rob_next = nums[N - 1]
        
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])
            
            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current
            
        return rob_next
        
