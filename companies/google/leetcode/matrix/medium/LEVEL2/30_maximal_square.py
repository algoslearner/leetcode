# https://leetcode.com/problems/maximal-square/
# google 3, amazon 4
'''
221. Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
'''

###########################################################################################################
# BRUTE FORCE
# TC: O((mn)^2)
# SC: O(1)
# https://leetcode.com/problems/maximal-square/discuss/817156/PythonEASY-Going-from-brute-force-to-DP-solution
# https://leetcode.com/problems/maximal-square/discuss/799521/Python-Short-Recursive-Solution-to-Optimized-DP

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        def helper(row, col):
            if row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == '0':
                return 0
            return 1+min(helper(row+1, col), helper(row, col+1), helper(row+1, col+1))
        
        
        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, helper(r,c))
        return res**2

###########################################################################################################
# dp
# TC: O(mn)
# SC: O(mn)
# https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 # Be careful of the indexing since dp grid has additional row and column
                    max_side = max(max_side, dp[r+1][c+1])
                
        return max_side * max_side

