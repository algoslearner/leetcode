# https://leetcode.com/problems/minimum-path-sum/
'''
64. Minimum Path Sum
Google 6, Amazon 8, Fb 2

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
'''

############################################################################################################
# BRUTE FORCE : TLE
# TC: O(2^(m+n))
# SC: O(m+n)

class Solution:
    def calculate(self, grid: List[List[int]], i: int, j: int)-> int:
        if i == len(grid) or j == len(grid[0]):
            return sys.maxsize
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]
        
        return grid[i][j] + min(self.calculate(grid, i+1, j), self.calculate(grid, i, j+1))
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.calculate(grid, 0, 0)
      
      
############################################################################################################
# DP using a 1D array extra space
# TC: O(mn)
# SC: O(m)

class Solution:    
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [0] * len(grid[0])
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
              
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    dp[j] = grid[i][j] + dp[j+1]
                    
                elif j == len(grid[0]) - 1 and i != len(grid) - 1:
                    dp[j] = grid[i][j] + dp[j]
                    
                elif j != len(grid[0]) - 1 and i != len(grid) - 1:
                    dp[j] = grid[i][j] + min(dp[j], dp[j + 1])
                    
                else:
                    dp[j] = grid[i][j]
        return dp[0]

############################################################################################################
# DP using no extra space
# TC: O(mn)
# SC: O(1)      

class Solution:    
    def minPathSum(self, grid: List[List[int]]) -> int:

        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    grid[i][j] = grid[i][j] + grid[i][j + 1]
                
                elif j == len(grid[0]) - 1 and i != len(grid) - 1:
                    grid[i][j] = grid[i][j] + grid[i+1][j]
                
                elif j != len(grid[0]) - 1 and i != len(grid) - 1:
                    grid[i][j] = grid[i][j] + min(grid[i+1][j], grid[i][j+1])
        
        return grid[0][0]
        
