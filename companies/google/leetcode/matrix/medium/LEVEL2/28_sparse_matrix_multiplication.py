# https://leetcode.com/problems/sparse-matrix-multiplication/
'''
Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. 

You may assume that multiplication is always possible.

 

Example 1:


Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output: [[7,0,0],[-7,0,3]]
Example 2:

Input: mat1 = [[0]], mat2 = [[0]]
Output: [[0]]
 

Constraints:

m == mat1.length
k == mat1[i].length == mat2.length
n == mat2[i].length
1 <= m, n, k <= 100
-100 <= mat1[i][j], mat2[i][j] <= 100
'''

###############################################################################################################
# NAIVE
# TC: O(m.k.n)
# SC: O(1)

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # Product matrix.
        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        
        for row_index, row_elements in enumerate(mat1):
            for element_index, row_element in enumerate(row_elements):
                # If current element of mat1 is non-zero then iterate over all columns of mat2.
                if row_element:
                    for col_index, col_element in enumerate(mat2[element_index]):
                        ans[row_index][col_index] += row_element * col_element
        
        return ans
###############################################################################################################
# READ for fb interview: https://leetcode.com/problems/sparse-matrix-multiplication/discuss/419538/What-the-interviewer-is-expecting-when-this-problem-is-asked-in-an-interview...
