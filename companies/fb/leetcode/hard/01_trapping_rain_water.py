'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''

# TC : O(N)
# SC : O(N)

import math

class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0] * len(height)
        rightmax = [0] * len(height)
        
        maxi = -math.inf
        for i in range(len(height)):
            leftmax[i] = max(maxi,height[i])
            maxi = leftmax[i]
        
        maxi = -math.inf
        for i in range(len(height)-1,-1,-1):
            rightmax[i] = max(maxi,height[i])
            maxi = rightmax[i]
        
        diff = 0
        for i in range(len(height)):
            diff += min(leftmax[i],rightmax[i]) - height[i]
        
        return diff
