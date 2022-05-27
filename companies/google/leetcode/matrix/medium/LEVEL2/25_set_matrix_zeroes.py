# https://leetcode.com/problems/set-matrix-zeroes/
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

#############################################################################################
# HASHSET
# TC: O(mn)
# SC: O(m+n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
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
                    
                    
#############################################################################################
# no extra space
# TC: O(mn)
# SC: O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(R):
                matrix[i][0] = 0

#############################################################################################
# 
# TC: O(mn)
# SC: O(1)
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
