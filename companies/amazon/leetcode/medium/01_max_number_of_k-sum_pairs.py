# https://leetcode.com/problems/max-number-of-k-sum-pairs/
'''
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
'''

#####################################################################################################
# USE HASH TABLE
# TC: O(n)
# SC: O(n)
# https://leetcode.com/problems/max-number-of-k-sum-pairs/discuss/2005967/Python-Two-easy-solutions

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = {}
        count = 0
        for n in nums:
            # if there is n in table and is not used
            complement = k - n
            if complement in hashmap and hashmap[complement] > 0:
                count += 1
                hashmap[complement] -= 1
            elif n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
            
        return count
      
#####################################################################################################
# TWO POINTERS
# TC: O(n log n)
# SC: O(1)

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        
        while left < right:
            cur = nums[left] + nums[right]
            if cur == k:
                count += 1
                left += 1
                right -= 1
            elif cur < k:
                left += 1
            else:
                right -= 1
        
        return count

