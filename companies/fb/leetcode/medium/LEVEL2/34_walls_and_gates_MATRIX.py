'''
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
 

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
'''

# BFS from gate to each empty space
# Time: O(NM)
# Space: O(NM)

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        
        h = len(rooms)
        w = len(rooms[0])
        
        q = deque()
        for i in range(h):
            for j in range(w):
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        while q:
            row, col = q.popleft()
            dist = rooms[row][col] + 1
            for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                r = row + dy
                c = col + dx
                if 0 <= r < h and 0 <= c < w and rooms[r][c] == 2147483647:
                    rooms[r][c] = dist
                    q.append((r,c))
