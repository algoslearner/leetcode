# https://leetcode.com/problems/pacific-atlantic-water-flow/
# google 11, fb 4
'''
417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west
if the neighboring cell's height is less than or equal to the current cell's height. 
Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result 
where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
'''

##############################################################################################################
# BFS
# TC: O(M.N)
# SC: O(M.N)
# "Water can only flow in four directions". Here water means, land water, not ocean water.
# Matrices such as this one are a type of graph representation. Standard graph traversal algorithms such as BFS and DFS can be used to solve this problem. 
'''
Algorithm

1. If the input is empty, immediately return an empty array.
2. Initialize variables that we will use to solve the problem:
      Number of rows and columns in our matrix;
      2 queues, one for the Atlantic Ocean and one for the Pacific Ocean that will be used for BFS;
      2 data structures, again one for each ocean, that we'll use to keep track of cells we already visited, to avoid infinite loops;
      A small array [(0, 1), (1, 0), (-1, 0), (0, -1)] that will help with BFS.
3. Figure out all the cells that are adjacent to each ocean, and fill the respective data structures with them.
4. Perform BFS from each ocean. The data structure used to keep track of cells already visited has a double purpose - it also contains every cell that can flow into that ocean.
5. Find the intersection, that is all cells that can flow into both oceans.
'''

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check if input is empty
        if not matrix or not matrix[0]: 
            return []
            
        num_rows, num_cols = len(matrix), len(matrix[0])

        # Setup each queue with cells adjacent to their respective ocean
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(num_rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, num_cols - 1))
        for i in range(num_cols):
            pacific_queue.append((0, i))
            atlantic_queue.append((num_rows - 1, i))
        
        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                # This cell is reachable, so mark it
                reachable.add((row, col))
                for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # Check all 4 directions
                    new_row, new_col = row + x, col + y
                    # Check if the new cell is within bounds
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    # Check that the new cell hasn't already been visited
                    if (new_row, new_col) in reachable:
                        continue
                    # Check that the new cell has a higher or equal height,
                    # So that water can flow from the new cell to the old cell
                    if matrix[new_row][new_col] < matrix[row][col]:
                        continue
                    # If we've gotten this far, that means the new cell is reachable
                    queue.append((new_row, new_col))
            return reachable
        
        # Perform a BFS for each ocean to find all cells accessible by each ocean
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))
