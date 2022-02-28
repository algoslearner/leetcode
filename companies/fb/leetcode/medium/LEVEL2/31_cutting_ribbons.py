'''
You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k. You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.

For example, if you have a ribbon of length 4, you can:
Keep the ribbon of length 4,
Cut it into one ribbon of length 3 and one ribbon of length 1,
Cut it into two ribbons of length 2,
Cut it into one ribbon of length 2 and two ribbons of length 1, or
Cut it into four ribbons of length 1.
Your goal is to obtain k ribbons of all the same positive integer length. You are allowed to throw away any excess ribbon as a result of cutting.

Return the maximum possible positive integer length that you can obtain k ribbons of, or 0 if you cannot obtain k ribbons of the same length.

 

Example 1:

Input: ribbons = [9,7,5], k = 3
Output: 5
Explanation:
- Cut the first ribbon to two ribbons, one of length 5 and one of length 4.
- Cut the second ribbon to two ribbons, one of length 5 and one of length 2.
- Keep the third ribbon as it is.
Now you have 3 ribbons of length 5.
Example 2:

Input: ribbons = [7,5,9], k = 4
Output: 4
Explanation:
- Cut the first ribbon to two ribbons, one of length 4 and one of length 3.
- Cut the second ribbon to two ribbons, one of length 4 and one of length 1.
- Cut the third ribbon to three ribbons, two of length 4 and one of length 1.
Now you have 4 ribbons of length 4.
Example 3:

Input: ribbons = [5,7,9], k = 22
Output: 0
Explanation: You cannot obtain k ribbons of the same positive integer length.
 

Constraints:

1 <= ribbons.length <= 105
1 <= ribbons[i] <= 105
1 <= k <= 109
'''

# https://leetcode.com/problems/cutting-ribbons/discuss/1580490/Python-or-Easy-to-Understand-or-Binary-Search-or-with-Explanation
'''
The crux of the problem is implementing Binary Search.
The goal is to figure out what the maximum length of a ribbon could be so that we get k ribbons of that max length.

One way to think of it would be that the ribbon length could be anywhere from 1 to the max length of the a ribbon available in the list.
So what we do is go through the list (using Binary Search since we need to optimize linear search), 
find the mid of the given array and then iterate through the list testing the length with each element 
and summing the number of ribbons that can be made with the mid value. Then change mid accordingly
'''

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # The minumum length of the ribbon that we can cut is 1
        start = 1
        # The maximum length of the ribbon can be the maximum element in the list
        end = max(ribbons)
        
        # In this binary search, we are trying to go through the origin list and figure out which integer(from 1 -> ribbon of max length) is the deired length for the the target k pieces
        while(start <= end):
            mid = start + (end - start) // 2
            res = 0
            for i in ribbons:
                res += i // mid
            # If the value is >= target, we know that there could be a larger integer that will satisfy the same conditon
            if res >= k:
                start = mid+1
            else:
            # If lesser than k, then there could be a value lesser than the mid that could satisfy the condition
                end = mid -1
        return end
