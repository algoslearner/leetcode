'''
write a function that finds a ship and return its coordinates: (battleship)
'''



##############################################################################
# Battleship count in a board (medium)
#
'''
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

 

Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.
 

Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
'''

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == 'X' 
                and (i == 0 or board[i-1][j] != 'X') 
                and (j == 0 or board[i][j-1] != 'X')) :
                    count += 1
        return count

       
#######################################################################################################
# NUMBER of ISLANDS
# This task is very similar to the task https://leetcode.com/problems/number-of-islands/, 
# but has more severe limitations in particular, ships are positioned only vertically or horizontally.
'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        r = len(grid)
        c = len(grid[0])
        if r == None: return 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count
    
    def dfs(self, grid: List[List[str]], r: int, c: int) -> None:
        rows = len(grid)
        col = len(grid[0])
        
        # mark visted nodes as zero
        grid[r][c] = '0'
        
        if (r - 1 >= 0 and grid[r-1][c] == '1'): self.dfs(grid, r-1, c)
        if (r + 1 < rows and grid[r+1][c] == '1'): self.dfs(grid, r+1, c)
        if (c - 1 >= 0 and grid[r][c-1] == '1'): self.dfs(grid, r, c-1)
        if (c + 1 < col and grid[r][c+1] == '1'): self.dfs(grid, r, c+1)


#######################################################################################################
# RETURN Co-ordinates of battleship
# https://leetcode.com/discuss/interview-question/618999/Facebook-or-Phone-or-Battleships-or-where-did-i-go-wrong

'''
The question was similar to battleships on the board, but I was asked to return the coordinates
for example we have

[["X",".",".","X"],
 [".",".",".","X"],
 [".",".",".","X"]]
You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships

output should be [(0,0)] [(0,3), (1,3), (2,3)} representing 2 ships on the board

My solution

out = []
for x in range(len(board)):
    for y in range(len(board[x])):
        
        if board[x][y] == 'X':
            out.append((x,y))
return out
'''
##############################################
# your task is almost the same as https://leetcode.com/problems/battleships-in-a-board/ 
# with the only difference being that you need to display an array of ship coordinates, and not just their number 
# and it is proposed not to modify the original array.

class Solution:
def countBattleships_(self, board: List[List[str]]) -> int:
    
    if not board or len(board) == 0 or len(board[0]) == 0:
        return 0
    
    cnt = 0
    self.ships = collections.defaultdict(list)
    
    def dfs(i,j,cnt):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '.':
            return
        
        self.ships[cnt].append((i,j))         
        board[i][j] = '.'
        dfs(i+1,j,cnt)
        dfs(i-1,j,cnt)
        dfs(i,j-1,cnt)
        dfs(i,j+1,cnt)
        
    for row in range(len(board)):
        for cell in range(len(board[0])):
            
            if board[row][cell] == 'X': 
                cnt += 1
                dfs(row,cell,cnt)
     
    print("Count ships: {}, coords: {}".format(cnt,list(self.ships.values())))
    return cnt
