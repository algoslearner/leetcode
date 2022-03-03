'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

'''

class Solution:
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        length = len(nums)
        left = 0
        right = length - 1
        while left <= right:
            mid = int((left + right) / 2)    
            
            if nums[mid] == target: 
                if isFirst:
                    # This means we found our lower bound.
                    if mid == left or nums[mid - 1] < target:
                        return mid
                    # Search on the left side for the bound.
                    right = mid - 1
                else:
                    
                    # This means we found our upper bound.
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    
                    # Search on the right side for the bound.
                    left = mid + 1
            
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # two binary searches
        # TC: O(log N)
        # SC: O(1)
        
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        return [lower_bound, upper_bound]
