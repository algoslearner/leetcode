'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # SORT
        # Time: O(n log n)
        # Space: O(1)
        '''
        nums.sort()
        
        # corner case
        if len(nums)==1:
            return nums[0]

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                # mid points
                if i+1 < len(nums) and nums[i] != nums[i+1]:
                    return nums[i]
                # start
                if i-1 == 0:
                    return nums[i-1]
                # end
                if i == len(nums)-1:
                    return nums[i]
          
        '''  
        '''
        # STACK
        # Time : O(n)
        # Space : O(n)
        stack = []
        for i in nums:
            if stack and i in stack:
                stack.remove(i)
            else:
                stack.append(i)
        return stack[-1]
        '''
        
        # BIT MANIPULATION
        # Time : O(n)
        # Space : O(1)
        
        a = 0
        for i in nums:
            a ^= i
        return a                
