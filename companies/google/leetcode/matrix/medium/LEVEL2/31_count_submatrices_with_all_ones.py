# https://leetcode.com/problems/count-submatrices-with-all-ones/
# google 3
'''
1504. Count Submatrices With All Ones

Given an m x n binary matrix mat, return the number of submatrices that have all ones.

 

Example 1:


Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
Explanation: 
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:


Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
Output: 24
Explanation: 
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
 

Constraints:

1 <= m, n <= 150
mat[i][j] is either 0 or 1.
'''

########################################################################################################
# HASHSET
# TC: O(MN)
# SC: O(M)

'''
# https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/723109/Python-solution
loop through each row. use a list to record the height of each column, 
and a stack to record the height and the # of additional submatrices created by column for each row

if the height of the cur column< that of the previous column in the stack, 
pop the record of the previous column from the stack until either the stack is empty or the previous column has a lower height

the ＃of additional submatrices created by the cur column equals 
(the index of the cur column - the index of the previous column with lower height)* the height of cur column, 
plus the submatries owing to the previous column with lower height
'''
# READ : https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/720265/Java-Detailed-Explanation-From-O(MNM)-to-O(MN)-by-using-Stack

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        col=len(mat[0])
        h,res=[0]*col,0
        
        for row in mat:
            memo=[] 
            for i in range(col):
                h[i]=(row[i]==1)*(h[i]+1)
                
                while memo and h[i]<h[memo[-1][0]]:
                    memo.pop()
                    
                ct = (i-memo[-1][0])*h[i]+memo[-1][1] if memo else h[i]*(i+1)
                
                res += ct    
                memo.append((i,ct)) #(index, additonal submatrices)
                
        return res

####################################################################################################
# 
# https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/721599/Clean-Code-Python-O(-M2-N-)-time-O(-N-)-space
'''
Clean Code - Python - O( M^2 N ) time, O( N ) space

Algorithm adapted from the "Progressive Scanning" Method described in "Cracking the Coding Interview" (Hard Problem 17.24 Max Submatrix).

Now instead of looking for the largest sum, our scanning function counts the number of valid rectangles found for a given height.
'''

class Solution:
    def scan(self, arr,height):
        _sum, found = 0, 0
        for x in arr:
            _sum = 0 if x<height else (_sum+1)
            if _sum:
                found += _sum
        return found
    
    def numSubmat(self, mat: List[List[int]]) -> int:
        r, result = len(mat), 0
        for i in range(r):
            row     = mat[i]
            result += self.scan(row,1)
            for k in range(i+1,r):
                row = [ x + mat[k][j] for j,x in enumerate(row) ]
                result += self.scan(row,k-i+1)
        return result
