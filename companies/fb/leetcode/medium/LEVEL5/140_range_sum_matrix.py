'''
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
 

Example 1:


Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-105 <= matrix[i][j] <= 105
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.
'''

############################################################################################################
# https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/746401/In-place-Python-O(1)-solution-(easy-explanation-with-image)

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # make prefix sums for rows
        for row in range(len(matrix)):
            for col in range(1, len(matrix[0])):
                matrix[row][col] = matrix[row][col - 1] + matrix[row][col]
                
        # make prefix sums for regions
        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] = matrix[row][col] + matrix[row - 1][col]
        self.matrix = matrix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        current_region_sum = self.matrix[row2][col2]
        origin = self.matrix[row1 - 1][col1 - 1] if row1 != 0 and col1 != 0 else 0
        left_region_sum = self.matrix[row2][col1 - 1] if col1 != 0 else 0
        top_region_sum = self.matrix[row1 - 1][col2] if row1 != 0 else 0
        return current_region_sum - top_region_sum - left_region_sum + origin
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
