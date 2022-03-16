'''
Searching algorithms
 1. (*high frequency question) Generate a minesweeper grid (2x3) with 3 randomly-placed mines (solution)

Implement Minesweeper
Minesweeper is a game where the objective is correctly identify the location of all mines in a given grid. 
You are given a uniform grid of gray squares in the beginning of the game. 
Each square contains either a mine (indicated by a value of 9), or an empty square. 
Empty squares have a number indicating the count of mines in the adjacent squares. 
Empty squares can have counts from zero (no adjacent mines) up to 8 (all adjacent squares are mines).
If you were to take a complete grid, for example, you can see which squares have mines and which squares are empty:

'''

######################################################################################################
# minesweeper (medium)
# https://leetcode.com/problems/minesweeper/
'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
'''

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




