# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
'''

##############################################################################################################################
# two pointers
# TC: O(N)
# SC: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            twosum = numbers[left] + numbers[right]
            if twosum == target:
                return [left+1, right+1]
            elif twosum < target:
                left += 1
            else:
                right -= 1
        return []