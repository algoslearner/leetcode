# https://leetcode.com/problems/shortest-bridge/
'''
934. Shortest Bridge

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
'''

############################################################################################################
'''
# https://leetcode.com/problems/shortest-bridge/discuss/1920292/DFS-%2B-BFS-SOLUTION-EXPLAIN-PROPELRY-EASY-TO-UNDERSTAND
Explaination : 
fist using dfs mark all the value of first iland as 2
then we know that there are only two ilands in the question so all the remaining 1's are of 2nd iland so add all them in queue
pass this queue in BFS and bsf will find the minimum path to iland one i.e the value we mark as 2 if use this as condition of return
note in return of the final ans I have substract -1 bcz in BFS I have added distace for 2 also.
'''

class Solution:
	def shortestBridge(self, grid: List[List[int]]) -> int:
		q, n, count = deque(), len(grid), 0
		
		#used dfs to mark all one's of first iland as 2
		def dfs(i,j):
			if 0<=i<n and 0<=j<n and grid[i][j] == 1:
				grid[i][j] = 2
				dfs(i,j-1) or dfs(i,j+1) or dfs(i+1,j) or dfs(i-1,j)
				
		#used bfs to find the min distance between iland
		def bfs(q):
			visited = set()
			while q:
				i, j, dist = q.popleft()
				if grid[i][j] == 2:
					return dist

				for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
					if 0<=x<n and 0<=y<n and (x,y) not in visited :
						visited.add((x,y))
						q.append((x,y,dist+1))

		for i in range(n):
			for j in range(n):
				if grid[i][j] == 1:
					if count == 0:         #due to this conditon dfs run for only first iland
						count += 1
						dfs(i,j)
					else :
						q.append((i,j,0))          #appending all one's of second iland in queue to use bfs 
		return bfs(q) - 1
