'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''



class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # TC: O(n+m)
        # SC: O(n+m)
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)
      
'''
This is a Facebook interview question.
They ask for the intersection, which has a trivial solution using a hash or a set.

Then they ask you to solve it under these constraints:
O(n) time and O(1) space (the resulting array of intersections is not taken into consideration).
You are told the lists are sorted.

Cases to take into consideration include:
duplicates, negative values, single value lists, 0's, and empty list arguments.
Other considerations might include
sparse arrays.
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Two pointers, for initially sorted arrays
        # TC: O(n)
        # SC: O(1)
        i = 0
        j = 0
        res = set()
        nums1.sort()
        nums2.sort()
        while( i < len(nums1) and j < len(nums2) ):
            if nums1[i] < nums2[j]:
                i += 1
                continue
            if nums1[i] > nums2[j]:
                j += 1
                continue
            res.add(nums1[i])
            i += 1
            j += 1
        return res
