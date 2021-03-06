'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 

Follow up: Could you find an O(n + m) solution?
'''

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        # BRUTE FORCE
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] < 0:
                    count += 1
        return count
  
  # https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/discuss/1041953/Python-O(m%2Bn)-solution-with-explanation
  '''
  The key phrase here is non-increasing order. This means:

The next value in each row is lesser than or equal to the current value (i.e. grid[row][col+1] <= grid[row][col])
The value in the next row at the same col will either be lesser than or equal to the current value (i.e. grid[row+1][col] <= grid[row][col])
Therefore, we don't have to iterate through every value of each row to identify if it is lesser than 0.

The following conditions would suffice:

if the particular value of grid[row][col] < 0, then all the following rows at the same col index will be negative.
move col index left and verify condition as stated above
if condition is not met, move down one row
repeat conditions listed above
'''
 
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        # return str(grid).count('-')
        
        # BRUTE FORCE
        # TC : O(n*m)
        # SC : O(1)
        '''
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] < 0:
                    count += 1
        return count
        '''
        
        # SEARCH ROW By ROW
        # TC: O(n+m)
        # SC : O(1)
        n = len(grid[0])  # O(n)
        row = len(grid)-1  # O(m)
        col = 0
        count = 0
        while row >= 0 and col < n:  # O(n) + O(m)
            if grid[row][col] < 0:
                count += n - col
                row -= 1
            else:
                col += 1
        return count
    
