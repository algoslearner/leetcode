'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
'''

##################################################################################################
# OPTIMIZED : Walk the spiral
# TC: O(n^2)
# SC: O(1)

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0] * n for _ in range(n)]
        cnt = 1
        
        for layer in range((n+1)//2):
            # direction 1 - traverse from left to right
            for i in range(layer, n - layer):
                output[layer][i] = cnt
                cnt += 1
            
            # direction 2 - traverse from top to bottom
            for i in range(layer + 1, n - layer):
                output[i][n - layer - 1] = cnt
                cnt += 1
                
            # direction 3 - traverse from right to left
            for i in range(layer + 1, n - layer):
                output[n - layer - 1][n - i - 1] = cnt
                cnt += 1
            
            # direction 4 - traverse from bottom to top
            for i in range(layer + 1, n - layer - 1):
                output[n - i - 1][layer] = cnt
                cnt += 1
                
        return output

##################################################################################################
# OPTIMIZED : Walk the spiral
# TC: O(n^2)
# SC: O(1)
# https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions
# Initialize the matrix with zeros, then walk the spiral path and write the numbers 1 to n*n. Make a right turn when the cell ahead is already non-zero.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        
        for k in range(n * n):
            output[i][j] = k + 1
            
            if output[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return output
