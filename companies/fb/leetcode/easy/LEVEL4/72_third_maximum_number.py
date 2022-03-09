'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Can you find an O(n) solution?
'''

'''
related question: K-th largest number in an array
'''

# READ:
# https://leetcode.com/problems/third-maximum-number/solution/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # use set for storing 3 maximums
        # TC: O(N), SC: O(1), since we are only storing 3 numbers at a time
        maximums = set()
        for num in nums:
            maximums.add(num)
            if len(maximums) > 3:
                maximums.remove(min(maximums))
        
        if len(maximums) == 3:
            return min(maximums)
        else:
            return max(maximums)
