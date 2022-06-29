# https://leetcode.com/problems/largest-rectangle-in-histogram/
# amazon 19, 
'''
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''

##############################################################################################################
# brute force
# TC: O(n^2)
# SC: O(1)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        for i in range(len(heights)):
            min_height = float('inf')
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                area = min_height * (j - i + 1)
                maxarea = max(maxarea, area)
        
        return maxarea
      
##############################################################################################################
# stack
# TC: O(n)
# SC: O(n)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []
        heights.append(0)
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                base = i if not stack else i - stack[-1] - 1
                maxarea = max(maxarea, h * base)
            stack.append(i)
                
        
        return maxarea
