'''
Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares ' '.
The first player always places 'X' characters, while the second player always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
 

Example 1:


Input: board = ["O  ","   ","   "]
Output: false
Explanation: The first player always plays "X".
Example 2:


Input: board = ["XOX"," X ","   "]
Output: false
Explanation: Players take turns making moves.
Example 3:


Input: board = ["XOX","O O","XOX"]
Output: true
 

Constraints:

board.length == 3
board[i].length == 3
board[i][j] is either 'X', 'O', or ' '.
'''

###############################################################################################################
# https://leetcode.com/problems/valid-tic-tac-toe-state/discuss/479695/concise-code-beat-100-python-solution-with-explanation
'''
There is only four situation that Tic-Tac-Toe is invalid:

two players are not taking turns making move
"O" player makes move before "X" player
"X" player wins but "O" player continues to make move
"O" player wins but "X" player continues to make move
'''

class Solution(object):
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(s): # return True if the player who use s wins
            if board[0][0]==s and board[0][1]==s and board[0][2]==s: return True
            if board[1][0]==s and board[1][1]==s and board[1][2]==s: return True
            if board[2][0]==s and board[2][1]==s and board[2][2]==s: return True
            if board[0][0]==s and board[1][0]==s and board[2][0]==s: return True
            if board[0][1]==s and board[1][1]==s and board[2][1]==s: return True
            if board[0][2]==s and board[1][2]==s and board[2][2]==s: return True
            if board[0][0]==s and board[1][1]==s and board[2][2]==s: return True
            if board[0][2]==s and board[1][1]==s and board[2][0]==s: return True
            return False
        
        xNo, oNo=0, 0
        for row in board:
            xNo+=row.count('X')
            oNo+=row.count('O')
        if oNo>xNo or xNo-oNo>=2: # "X" not making move first or not taking turns making move
            return False
        if xNo>=3:
            if xNo==oNo and win('X'): # put another "O" after "X" player winning
                return False
            if xNo!=oNo and win('O'): # put another "X" after "O" player winning
                return False
        return True
        
