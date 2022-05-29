# https://leetcode.com/problems/maximum-subarray/
'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

########################################################################################################
# Greedy : brute force
# TC: O(n)
# SC: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        currsum = 0
        
        for n in nums:
            currsum += n
            maxsum = max(maxsum, currsum)
            if currsum < 0:
                currsum = 0
        
        return maxsum
        
########################################################################################################
# Kadane's algorithm
# TC: O(n)
# SC: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        maxsum = nums[0]
        currsum = nums[0]
        for n in nums[1:]:
            currsum = max(n, currsum + n)
            maxsum = max(maxsum, currsum)
        return maxsum
        
########################################################################################################
# Divide and conquer
# TC: O(n log n)
# SC: O(log n)
# https://leetcode.com/problems/maximum-subarray/discuss/1234480/Python-or-O(n.logn)-Divide-and-Conquer-or-O(n)-using-Kadane's-Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)
        
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)
