'''
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99
 

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
'''

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        # BRUTE FORCE
        # Time : O(N*M)
        # Space: O(1)
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i-1][j-1] != matrix[i][j]:
                    return False
        return True
    
    # FOLLOW UP - 1 : memory limited. can only read matrix one row at a time
    # FOLLOW UP - 2 : matrix is so large, can only load up a partial row to memory once


# https://leetcode.com/problems/toeplitz-matrix/discuss/1607862/Python-Easy-%3A-Efficient-Solution-%3A-Trick
'''
Let m be rows and n be the columns of the matrix.
For each row, we can observe that first n-1 cols are equivalent to next row's last n-1 cols.
So we can compare them for each row in the matrix.
'''
# Time: O(N)
# Space : O(1)

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows-1):
            if matrix[i][:cols-1] != matrix[i+1][1:cols]:
                return False
        return True
  
  
  
