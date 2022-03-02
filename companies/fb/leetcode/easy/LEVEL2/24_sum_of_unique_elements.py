'''
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

 

Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''

# HASHMAP
# TC : O(n)
# SC : O(n)

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashMap = {}
        for i in nums:
            if hashMap and i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        
        uniqSum = 0
        for key, val in hashMap.items():
            if val == 1:
                uniqSum += key
        return uniqSum
