'''
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

 

Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:


Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
'''

#########################################################################################
# TC: O(nmk)
# SC: O(nm)

def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

    num_rows, num_cols = len(grid), len(grid[0])

    for _ in range(k):
        # Create a new grid to copy into.
        new_grid = [[0] * num_cols for _ in range(num_rows)]

        # Case 1: Move everything not in the last column.
        for row in range(num_rows):
            for col in range(num_cols - 1):
                new_grid[row][col + 1] = grid[row][col]

        # Case 2: Move everything in last column, but not last row.
        for row in range(num_rows - 1):
             new_grid[row + 1][0] = grid[row][num_cols - 1]

        # Case 3: Move the bottom right.
        new_grid[0][0] = grid[num_rows - 1][num_cols - 1]

        grid = new_grid

    return grid
  
  
#########################################################################################
# use modulo shift
# TC: O(nm)
# SC: O(nm)

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
            
        num_rows = len(grid)
        num_cols = len(grid[0])
        for i in range(num_rows):
            for j in range(num_cols):
                new_col = (j + k) % num_cols
                wrap_count = (j + k) // num_cols
                new_row = (i + wrap_count) % num_rows
                new_grid[new_row][new_col] = grid[i][j]
        return new_grid
                
  
