'''
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

 

Example 1:


Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
Example 2:


Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i].length <= 105
1 <= sum(nums[i].length) <= 105
1 <= nums[i][j] <= 105
'''

###############################################################################################################
# https://leetcode.com/problems/diagonal-traverse-ii/discuss/597741/Clean-Simple-Easiest-Explanation-with-a-picture-and-code-with-comments
# Key Idea: In a 2D matrix, elements in the same diagonal have same sum of their indices.
'''
Algorithm

Insert all elements into an appropriate bucket i.e. nums[i][j] in (i+j)th bucket.
For each bucket starting from 0 to max, print all elements in the bucket.
Note: Here, diagonals are from bottom to top, but we traversed the input matrix from first row to last row. Hence we need to print the elements in reverse order.
'''

from collections import defaultdict 
from collections import deque

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(deque)
        for i, row in enumerate(nums):
            for j, e in enumerate(row):
                d[i+j].appendleft(e)
        trav = []
        for key, diag in d.items():
            trav.extend(diag)
        return trav
