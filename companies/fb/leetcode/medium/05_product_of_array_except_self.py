'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

# TC :O(n)
# SC : O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        R = 1
        output = [1] * len(nums)
		
        for i in range(1, len(nums)):
            output[i] = nums[i-1] * output[i-1]
			
        for j in range(len(nums)-1, -1, -1):
            output[j] = R * output[j]
            R = R * nums[j]
			
        return output
        

# LEFT and RIGHT PRODUCT LISTS
# TC: O(n)
# SC: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        
        # Constructing the answer array
        for i in range(length):
            answer[i] = L[i] * R[i]
        
        return answer
