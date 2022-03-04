'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
'''

# https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/785937/O(N)-Time-and-O(1)-Solution-Explained-With-a-Video-or-Easy-Code

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # TC: O(n)
        # SC: O(1) without calculating the output array
        rs = []
        for num in nums:
            num = abs(num)
            if nums[num-1] < 0:
                rs.append(num)
            else:
                nums[num-1] = -nums[num-1]
        return rs
