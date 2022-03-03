'''
FB HashTable: 160 times in past 6 months

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # TC : O(n2)
        # SC : O(1)
        '''
        count = 0
        length = len(nums)
        for start in range(length):
            window_sum = 0
            for end in range(start,length):
                window_sum += nums[end]
                if window_sum == k: count += 1
        return count
        '''
        
        # using hashmap
        # TC : O(n)
        # SC : O(n)
        cumulativeSum = 0
        freqMap = {}
        result = 0
        for num in nums:
            key = k + cumulativeSum
            freqMap[key] = freqMap.get(key, 0) + 1
            cumulativeSum += num
            if cumulativeSum in freqMap:
                result += freqMap[cumulativeSum]
        return result
                
