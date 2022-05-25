# https://leetcode.com/problems/special-positions-in-a-binary-matrix/
'''
1582. Special Positions in a Binary Matrix

Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

Example 1:


Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:


Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
'''

##################################################################################################
# TC: O(mn)
# SC: O(m + n)

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        special_count = 0
        
        rowtotals = []
        for row in mat:
            rowtotals.append(sum(row))
        
        coltotals = []
        for col in zip(*mat):
            coltotals.append(sum(col))
            
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rowtotals[i] == 1 and coltotals[j] == 1:
                    special_count += 1
        
        return special_count
