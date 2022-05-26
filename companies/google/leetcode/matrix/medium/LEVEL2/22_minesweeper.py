# https://leetcode.com/problems/minesweeper/
'''
529. Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

Example 1:


Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
Example 2:


Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 50
board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
click.length == 2
0 <= clickr < m
0 <= clickc < n
board[clickr][clickc] is either 'M' or 'E'.
'''

##########################################################################
# one way
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # DFS
        (row, col), directions = click, ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
        
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            if board[row][col] == 'M':
                board[row][col] = 'X'
            elif board[row][col] == 'E':
                n = sum([board[row + r][col + c] == 'M' for r, c in directions if 0 <= row + r < len(board) and 0 <= col + c < len(board[0])])
                board[row][col] = str(n if n else 'B')
                if not n:
                    for r, c in directions:
                        self.updateBoard(board, [row + r, col + c])
        return board

       
#########################################################################
# below implementation is easier to understand
##################################
# https://leetcode.com/problems/minesweeper/discuss/99826/Java-Solution-DFS-%2B-BFS
'''
This is a typical Search problem, either by using DFS or BFS. Search rules:

If click on a mine ('M'), mark it as 'X', stop further search.
If click on an empty cell ('E'), depends on how many surrounding mine:
2.1 Has surrounding mine(s), mark it with number of surrounding mine(s), stop further search.
2.2 No surrounding mine, mark it as 'B', continue search its 8 neighbors.
'''

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i = click[0]
        j = click[1]
        # found mine
        if board[i][j] == 'M':
            board[i][j] = 'X'
        else:
            self.updateOneSquare(board, i , j)
        return board
    
    def updateOneSquare(self,board: List[List[str]], i: int, j: int ) -> None:
        # check for invalid cases
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'E'):
            return
        
        nearby_mines_num = self.findNearbyMinesNumber(board, i, j)
        if nearby_mines_num > 0:
            board[i][j] = str(nearby_mines_num)
        else:
            board[i][j] = 'B'
            self.updateOneSquare(board, i - 1, j - 1)
            self.updateOneSquare(board, i - 1, j)
            self.updateOneSquare(board, i - 1, j + 1)
            self.updateOneSquare(board, i, j - 1)
            self.updateOneSquare(board, i, j + 1)
            self.updateOneSquare(board, i + 1, j - 1)
            self.updateOneSquare(board, i + 1, j)
            self.updateOneSquare(board, i + 1, j + 1)
            
    def findNearbyMinesNumber(self, board: List[List[str]], i: int, j: int) -> int:
        nearby_mines = self.hasMine(board, i - 1, j - 1) + self.hasMine(board, i - 1, j) + self.hasMine(board, i - 1, j + 1) + self.hasMine(board, i, j - 1) + self.hasMine(board, i, j + 1) + self.hasMine(board, i + 1, j - 1) + self.hasMine(board, i + 1, j) + self.hasMine(board, i + 1, j + 1)
        return nearby_mines
            
    def hasMine(self, board: List[List[str]], i: int, j: int) -> int:
        # invalid cases
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 0
        
        if board[i][j] == 'M':
            return 1
        else:
            return 0
