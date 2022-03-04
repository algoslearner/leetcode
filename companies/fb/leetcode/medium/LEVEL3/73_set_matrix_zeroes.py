'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # using set, TC: O(MN), SC: O(M+N)
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0
                    
                    
############################
'''
O(1) solution, Why we need a list to remember rows and cols?
We can directly set the matrix row, col to a flag value like 9999.
So here is the O(1) solution:
'''

class Solution:
# @param matrix, a list of lists of integers
# RETURN NOTHING, MODIFY matrix IN PLACE.
def setZeroes(self, matrix):
    def setMatrix(row,col,matrix,val):
        matrix[row][col]=val;
        for i in range(len(matrix[0])):
            if(matrix[row][i]!=9999): # key point, to skip the other 9999, so we can process it later.
                matrix[row][i]=val;
        for i in range(len(matrix)):
            if(matrix[i][col]!=9999):
                matrix[i][col]=val;

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j]==0):
               matrix[i][j]=9999;

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j]==9999):
               setMatrix(i,j,matrix,0);
