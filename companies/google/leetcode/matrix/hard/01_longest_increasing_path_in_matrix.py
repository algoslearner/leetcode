# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
'''
329. Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1

'''

########################################################################################################
# DFS naive
# TC: O(mn)
# SC: O(mn)
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/1151224/Python-by-DFS-%2B-memo-w-Hint

class Solution:
    def longestIncreasingPath(self, matrix):
        
        # -------------------------------------------
        def dfs( cur_position ):
            
            
            ## base case aka stop condition:
            if cur_position in table:
                
                # Quick response if cur_position has been explorered
                return table[cur_position]
            
            ## general cases:
            # visit each possible neighbor to compute longest increasing path
            
            longest_length = 0
            for next_pos in (cur_position + 1, cur_position - 1 , cur_position + 1j, cur_position - 1j ):
                
                if next_pos in grids and grids[next_pos] > grids[cur_position]:
                    
                    longest_length = max(longest_length, dfs(next_pos))
            
            # update memoization table, and 1 is the length of current position
            table[cur_position] = 1 + longest_length
            return table[cur_position]
        
        # -------------------------------------------
        
        # memoization for dfs
        table = {}
        
        ## dictionary
        # key: (X + Yj), 2D coordination in matrix. (j is imaginary part to present y axis in 2D coordination)
        # value: corresponding matrix value to (X, Y)
        grids = { x + y * 1j: value for y, row in enumerate(matrix) for x, value in enumerate(row) }
        
        # start DFS on each possible 2D coordination in grids
        return max( map(dfs, grids) )

########################################################################################################
# DP + memoization
# TC: O(mn)
# SC: O(mn)
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78334/Python-solution-memoization-dp-288ms
# We can find longest decreasing path instead, the result will be the same. Use dp to record previous results and choose the max dp value of smaller neighbors.

def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

    # corner case
    if not matrix or not matrix[0]:
        return 0

    # initilization
    M, N = len(matrix), len(matrix[0]) # length, width
    dp = [[0]*N for i in range(M)] # 2-D matrix for store the number of steps

    # dfs function
    def dfs(i, j):
        if not dp[i][j]: # if this position is not visited
            val = matrix[i][j]
            # search four directions to find out the decreasing path
            # up
            if i and val > matrix[i-1][j]:
                up = dfs(i-1, j)
            else:
                up = 0
            # down
            if i < M-1 and val > matrix[i+1][j]:
                down = dfs(i+1, j)
            else:
                down = 0
            # left
            if j and val > matrix[i][j-1]:
                left = dfs(i, j-1)
            else:
                left = 0
            # right
            if j < N-1 and val > matrix[i][j+1]:
                right = dfs(i, j+1)
            else:
                right = 0
            # "walk" to the target neighbor and accumulate the number of steps
            dp[i][j] = 1 + max(up, down, left, right)
        return dp[i][j]

    res_path = []
    for x in range(M): # search the grid by dfs
        for y in range(N):
            res_path.append(dfs(x, y))

    return max(res_path)

########################################################################################################
# Topological sort + DAG
# TC: O(mn)
# SC: O(mn)
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/288520/Longest-Path-in-DAG
'''
We regard
a cell in the matrix as a node,
a directed edge from node x to node y if x and y are adjacent and x's value < y's value
Then a graph is formed.

No cycles can exist in the graph, i.e. a DAG is formed.
The problem becomes to get the longest path in the DAG.
Topological sort can iterate the vertices of a DAG in the linear ordering.
Using Kahn's algorithm(BFS) to implement topological sort while counting the levels can give us the longest chain of nodes in the DAG.
'''

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0
        
        cols = len(matrix[0])
        indegree = [[0 for x in range(cols)] for y in range(rows)] 
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        for x in range(rows):
            for y in range(cols):
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                        if matrix[nx][ny] < matrix[x][y]:
                            indegree[x][y] += 1
                            
        queue = []
        for x in range(rows):
            for y in range(cols):
                if indegree[x][y] == 0:
                    queue.append((x, y))
    
        path_len = 0
        while queue:
            sz = len(queue)
            for i in range(sz):
                x, y = queue.pop(0)
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                        if matrix[nx][ny] > matrix[x][y]:
                            indegree[nx][ny] -= 1
                            if indegree[nx][ny] == 0:
                                queue.append((nx, ny))
            path_len += 1
        return path_len 
