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

# https://leetcode.com/problems/unique-paths/discuss/254228
#########################################################################################################
# bottom up DP
# TC: O(mn) 
# SC: O(min(m,n))
'''
Solution 1: Bottom up DP
1. Let dp[r][c] is number of paths to move from [0, 0] to [r, c].
2. Then dp[m-1][n-1] is our result.
3. There are maximum 2 ways to cell (r, c), that is:
     From upper cell, dp[r][c] += dp[r-1][c]
     From left cell, dp[r][c] += dp[r][c-1]
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = 1
                elif r == 0:
                    dp[r][c] = dp[r][c-1]
                elif c == 0:
                    dp[r][c] = dp[r-1][c]
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]

#########################################################################################################
# bottom up DP - optimized space
# TC: O(mn) 
# SC: O(min(m,n))
# Since we only access 2 states: current state dp and previous state dpPrev, we can reduce the space complexity to O(M).

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp, dpPrev = [0] * n, [0] * n
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[c] = 1
                elif r == 0:
                    dp[c] = dp[c-1]
                elif c == 0:
                    dp[c] = dpPrev[c]
                else:
                    dp[c] = dpPrev[c] + dp[c-1]
            dpPrev = dp
        return dpPrev[n-1]
       
# or

class Solution(object):
    def uniquePaths(self, m, n):
        # ensure m is smaller
        if m > n:
            m, n = n, m
        
        arr = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                arr[j] += arr[j-1] 
            
        return arr[-1]
       
# https://leetcode.com/problems/unique-paths/discuss/254228
#########################################################################################################
# MATH
# TC: O(m + n)
# SC: O(1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, n - 1)
   
# or

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n-2) // factorial(n-1) // factorial(m-1)
   
# or

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = 1
        j = 1
        for i in range(m, m+n-2 + 1):
            ans *= i
            ans //= j
            j += 1
            
        return ans
