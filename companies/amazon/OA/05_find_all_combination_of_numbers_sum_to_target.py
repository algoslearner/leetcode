########################################################################################################################
# Amazon OA question: https://leetcode.com/discuss/interview-question/1180017/Amazon-OA/1171090
'''
prob 1:
https://algo.monster/problems/amazon_oa_find_all_combination_of_numbers_sum_to_target
Should be O(N^3). I did not pass the tests per TLE
'''

########################################################################################################################
# Related leetcode question: https://leetcode.com/problems/4sum-ii/

'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
'''

########################################################################################################################
# USING DICT
# TC: O(N^2)
# SC: O(N^2)

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        m = collections.defaultdict(int)
        for a in nums1:
            for b in nums2:
                m[a + b] += 1
                
        for c in nums3:
            for d in nums4:
                cnt += m[-(c + d)]
                
        return cnt
