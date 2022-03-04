'''
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104
'''

# REFER
# Here is link for 523[https://leetcode.com/problems/continuous-subarray-sum/]
# The solution is familiar from https://leetcode.com/problems/subarray-sum-equals-k/

# USING HASHMAP
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        d = {0: 1}
        len_A = len(nums)
        acc = 0        
        for i in range(len_A):
            acc += nums[i]       
            key = acc % k
            
            if key in d:
                ans += d[key]
                d[key] += 1
            else:
                d[key] = 1
            
        return ans

# MORE OPTIMIZED: REPLACE HASHMAP with ARRAY in this case
# https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/217985/JavaC%2B%2BPython-Prefix-Sum

def subarraysDivByK(self, A, K):
        res = 0
        prefix = 0
        count = [1] + [0] * K
        for a in A:
            prefix = (prefix + a) % K
            res += count[prefix]
            count[prefix] += 1
        return res
