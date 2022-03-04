'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

# https://leetcode.com/problems/contiguous-array/discuss/653541/Python-HashMap-solution-%2B-Thinking-Process-Diagram

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        result = 0
        
        dict_seen = {}
        dict_seen[0] = -1
        
        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                count -= 1
            elif n == 1:
                count += 1
            
            if count in dict_seen:
                result = max(result,i-dict_seen[count])
            else:
                dict_seen[count] = i
        return result
