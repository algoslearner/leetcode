'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''

import math

def getTrappedRainWater(arr):
  # Write your code here
  leftmax = [0] * len(arr)
  rightmax = [0] * len(arr)
  
  maxvalue = -math.inf
  for i in range(len(arr)):
    leftmax[i] = max(maxvalue,arr[i])
    maxvalue = leftmax[i]
  
  maxvalue = -math.inf
  for i in range(len(arr)-1, -1, -1):
    rightmax[i] = max(maxvalue,arr[i])
    maxvalue = rightmax[i]
  
  # calculate trapped rain water
  ans = 0
  for i in range(len(arr)):
    ans += min(leftmax[i],rightmax[i]) - arr[i]
  
  return ans
