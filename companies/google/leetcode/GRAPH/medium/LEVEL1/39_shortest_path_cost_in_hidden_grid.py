# https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/
'''
1810. Minimum Path Cost in a Hidden Grid

This is an interactive problem.

There is a robot in a hidden grid, and you are trying to get it from its starting cell to the target cell in this grid. The grid is of size m x n, and each cell in the grid is either empty or blocked. It is guaranteed that the starting cell and the target cell are different, and neither of them is blocked.

Each cell has a cost that you need to pay each time you move to the cell. The starting cell's cost is not applied before the robot moves.

You want to find the minimum total cost to move the robot to the target cell. However, you do not know the grid's dimensions, the starting cell, nor the target cell. You are only allowed to ask queries to the GridMaster object.

The GridMaster class has the following functions:

boolean canMove(char direction) Returns true if the robot can move in that direction. Otherwise, it returns false.
int move(char direction) Moves the robot in that direction and returns the cost of moving to that cell. If this move would move the robot to a blocked cell or off the grid, the move will be ignored, the robot will remain in the same position, and the function will return -1.
boolean isTarget() Returns true if the robot is currently on the target cell. Otherwise, it returns false.
Note that direction in the above functions should be a character from {'U','D','L','R'}, representing the directions up, down, left, and right, respectively.

Return the minimum total cost to get the robot from its initial starting cell to the target cell. If there is no valid path between the cells, return -1.

Custom testing:

The test input is read as a 2D matrix grid of size m x n and four integers r1, c1, r2, and c2 where:

grid[i][j] == 0 indicates that the cell (i, j) is blocked.
grid[i][j] >= 1 indicates that the cell (i, j) is empty and grid[i][j] is the cost to move to that cell.
(r1, c1) is the starting cell of the robot.
(r2, c2) is the target cell of the robot.
Remember that you will not have this information in your code.

 

Example 1:

Input: grid = [[2,3],[1,1]], r1 = 0, c1 = 1, r2 = 1, c2 = 0
Output: 2
Explanation: One possible interaction is described below:
The robot is initially standing on cell (0, 1), denoted by the 3.
- master.canMove('U') returns false.
- master.canMove('D') returns true.
- master.canMove('L') returns true.
- master.canMove('R') returns false.
- master.move('L') moves the robot to the cell (0, 0) and returns 2.
- master.isTarget() returns false.
- master.canMove('U') returns false.
- master.canMove('D') returns true.
- master.canMove('L') returns false.
- master.canMove('R') returns true.
- master.move('D') moves the robot to the cell (1, 0) and returns 1.
- master.isTarget() returns true.
- master.move('L') doesn't move the robot and returns -1.
- master.move('R') moves the robot to the cell (1, 1) and returns 1.
We now know that the target is the cell (1, 0), and the minimum total cost to reach it is 2. 
Example 2:

Input: grid = [[0,3,1],[3,4,2],[1,2,0]], r1 = 2, c1 = 0, r2 = 0, c2 = 2
Output: 9
Explanation: The minimum cost path is (2,0) -> (2,1) -> (1,1) -> (1,2) -> (0,2).
Example 3:

Input: grid = [[1,0],[0,1]], r1 = 0, c1 = 0, r2 = 1, c2 = 1
Output: -1
Explanation: There is no path from the robot to the target cell.
 

Constraints:

1 <= n, m <= 100
m == grid.length
n == grid[i].length
0 <= grid[i][j] <= 100
'''

#####################################################################################################################################
# DFS + BFS
# TC:
# SC:
'''
# https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/discuss/1332485/Python-3-or-DFS-%2B-Dijkstra-or-Explanation

We don't know what the hidden grid looks like, so we want to find it out
First, "draw the grid" using DFS (we are not really drawing it, see more details below)
Then find the lowest cost to target using Dijkstra
'''

# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> int:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        opposite = {'D': 'U', 'U': 'D', 'L': 'R', 'R': 'L'}       # opposite direction to move back and force
        cost_dict = collections.defaultdict(lambda: sys.maxsize)  # save cost for each location (x, y)
        target = None                                             # this will be `target` index
        
        def dfs(cur, x, y):
            nonlocal target
            if cur.isTarget():                                    # if `target` found, save its index and return True
                target = x, y
                return True
            ans = False
            for di, (i, j) in zip(['D', 'U', 'L', 'R'], [(-1, 0), (1, 0), (0, -1), (0, 1)]): # explore 4 directions
                _x, _y = x+i, y+j
                if (_x, _y) in cost_dict: continue                # check if (_x, _y) is visited
                cost_dict[(_x, _y)] = sys.maxsize                 # mark (_x, _y) as visited
                if cur.canMove(di):
                    cost = cur.move(di)                           # move to direction `di`
                    cost_dict[(_x, _y)] = cost                    # save cost of (_x, _y)
                    ans |= dfs(cur, _x, _y)                       # `dfs`
                    cur.move(opposite[di])                        # move back
            return ans                    
        
        if not dfs(master, 0, 0): return -1                       # if can't reach to `target`, return -1
        
        heap = [(0, 0, 0)]                                        # starts from (0, 0) again. Parameters are (cost, x, y)
        while heap:                                               # Dijkstra starts here
            cost, x, y = heapq.heappop(heap)
            if (x, y) == target: return cost
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                _x, _y = x+i, y+j
                if (_x, _y) not in cost_dict: continue            # if location not in `cost_dict`, meaning it's not accessible
                heapq.heappush(heap, (cost+cost_dict[(_x, _y)], _x, _y))
                cost_dict[(_x, _y)] = sys.maxsize                 # mark as visited
        return -1



