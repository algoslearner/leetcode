'''
iven an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # extra space
        # TC : O(n)
        # SC : O(n)
        '''
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd
        '''
        
        # two pointers
        # TC : O(N)
        # SC : O(1)
        left = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            
        return nums
