# https://leetcode.com/problems/unique-paths/
# google 16, fb 10, amazon 8
'''
62. Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
'''

#########################################################################################################
# MATH
# TC:
# SC: O(1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, n - 1)
      
#########################################################################################################
# DP

# TC: O(mn) 
# DP solution doesn't have to hold the whole 2D array.
# Only one line needed, so the memory usage becomes O(min(M, N))

# SC: O(min(m,n))

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            m, n = n, m
        r = [1] * m
        for _ in range(1, n):
            for i in range(1, m):
                r[i] += r[i - 1]
        return r[-1]
