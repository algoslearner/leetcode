# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
'''
698. Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
 

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
'''

####################################################################################################################
# DP
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/274942/Python-DFS
# Have k buckets initialized with 0. Use DFS to try combination of all kinds of ∑nums[i]. Once it's exceed target=sum/k, the path failed.

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target,rem=divmod(sum(nums),k)
        if rem:
            return False
        nums.sort()
        if nums[-1]>target:
            return False
        
        def search(partitions):
            if not nums:
                return True
            v=nums.pop()
            for i,part in enumerate(partitions):
                if part+v<=target:
                    partitions[i]+=v
                    if search(partitions):
                        return True
                    partitions[i]-=v
                if not part:
                    nums.append(v)
                    return False
            nums.append(v)
            return False
        while nums and nums[-1]==target:
            nums.pop()
            k-=1
        return search([0]*k)
