'''
Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.

 

Example 1:

Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.
Example 2:

Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
 

Constraints:

1 <= nums.length <= 5 * 104
1 <= nums[i] <= 107
nums is sorted in ascending order, and all the elements are unique.
1 <= k <= 108
 

Follow up: Can you find a logarithmic time complexity (i.e., O(log(n))) solution?
'''

##############################################################################################
# Brute force
# TC: O(N)
# SC: O(1)

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        diff = 0
        
        for i in range(1,n):
            diff = nums[i] - nums[i-1] - 1
            
            if diff >= k:
                return nums[i-1] + k
            
            k -= diff
        
        return nums[n-1]+k
      
      
##############################################################################################
# OPTIMIZATION: BINARY SEARCH
# TC: O(n log n)
# SC: O(1)

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx
            
        n = len(nums)
        # If kth missing number is larger than 
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1) 
        
        left, right = 0, n - 1
        # find left = right index such that 
        # missing(left - 1) < k <= missing(left)
        while left != right:
            pivot = left + (right - left) // 2
            
            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot 
        
        # kth missing number is greater than nums[left - 1]
        # and less than nums[left]
        return nums[left - 1] + k - missing(left - 1) 
