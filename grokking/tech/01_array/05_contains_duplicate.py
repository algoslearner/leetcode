# https://leetcode.com/problems/contains-duplicate/
'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

#######################################################################################################################################

class Solution:
    # Time: O(n + log n) | Space: O(1)
    def containsDuplicate_sort(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
    # Time: O(n) | Space: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nummap = set()
        for num in nums:
            if num in nummap:
                return True
            nummap.add(num)
        return False
