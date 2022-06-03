# https://medium.com/codex/how-to-code-a-simple-chess-game-in-python-9a9cb584f57
# https://github.com/xsanon/chess

########################################################################################
# board.py

import piece

class Board():
    """
    A class to represent a chess board.
    ...
    Attributes:
    -----------
    board : list[list[Piece]]
        represents a chess board
        
    turn : bool
        True if white's turn
    white_ghost_piece : tup
        The coordinates of a white ghost piece representing a takeable pawn for en passant
    black_ghost_piece : tup
        The coordinates of a black ghost piece representing a takeable pawn for en passant
    Methods:
    --------
    print_board() -> None
        Prints the current configuration of the board
    move(start:tup, to:tup) -> None
        Moves the piece at `start` to `to` if possible. Otherwise, does nothing.
        
    """
    def __init__(self):
        """
        Initializes the board per standard chess rules
        """

        self.board = []

        # Board set-up
        for i in range(8):
            self.board.append([None] * 8)
        # White
        self.board[7][0] = piece.Rook(True)
        self.board[7][1] = piece.Knight(True)
        self.board[7][2] = piece.Bishop(True)
        self.board[7][3] = piece.Queen(True)
        self.board[7][4] = piece.King(True)
        self.board[7][5] = piece.Bishop(True)
        self.board[7][6] = piece.Knight(True)
        self.board[7][7] = piece.Rook(True)

        for i in range(8):
            self.board[6][i] = piece.Pawn(True)

        # Black
        self.board[0][0] = piece.Rook(False)
        self.board[0][1] = piece.Knight(False)
        self.board[0][2] = piece.Bishop(False)
        self.board[0][3] = piece.Queen(False)
        self.board[0][4] = piece.King(False)
        self.board[0][5] = piece.Bishop(False)
        self.board[0][6] = piece.Knight(False)
        self.board[0][7] = piece.Rook(False)

        for i in range(8):
            self.board[1][i] = piece.Pawn(False)


    def print_board(self):
        """
        Prints the current state of the board.
        """

        buffer = ""
        for i in range(33):
            buffer += "*"
        print(buffer)
        for i in range(len(self.board)):
            tmp_str = "|"
            for j in self.board[i]:
                if j == None or j.name == 'GP':
                    tmp_str += "   |"
                elif len(j.name) == 2:
                    tmp_str += (" " + str(j) + "|")
                else:
                    tmp_str += (" " + str(j) + " |")
            print(tmp_str)
        buffer = ""
        for i in range(33):
            buffer += "*"
        print(buffer)
        
########################################################################################
# piece.py

blocked_path = "There's a piece in the path."
incorrect_path = "This piece does not move in this pattern."


def check_knight(color, board, pos):
    """
    Check if there is a knight of the opposite `color` at
    position `pos` on board `board`. 
    color : bool
        True if white
    board : Board
        Representation of the current chess board
    pos : tup
        Indices to check if there's is a knight
    Precondition `pos` is a valid position on the board.
    """
    piece = board.board[pos[0]][pos[1]]
    if piece != None and piece.color != color and piece.name == 'N':
        return False
    return True


def check_diag_castle(color, board, start, to): 
    """
    Checks the diagonal path from `start` (non-inclusive) to `to` (inclusive)
    on board `board` for any threats from the opposite `color`
    color : bool
        True if white
    board : Board
        Representation of the current chess board
    start : tup
        Starting point of the diagonal path
    to : tup
        Ending point of the diagonal path
    Precondition: `start` and `to` are valid positions on the board
    """
    
    if abs(start[0] - to[0]) != abs(start[1] - to[1]):
        print(incorrect_path)
        return False

    x_pos =  1 if to[0] - start[0] > 0 else -1
    y_pos = 1 if to[1] - start[1] > 0 else -1

    i = start[0] + x_pos
    j = start[1] + y_pos
    
    exists_piece = board.board[i][j] != None
    if exists_piece and (board.board[i][j].name == 'P' or board.board[i][j].name == 'K') and \
        board.board[i][j].color != color:
        return False

    while (i <= to[0] if x_pos==1 else i >= to[0]):
        if exists_piece and board.board[i][j].color != color:
            if board.board[i][j].name in ['B', 'Q']: 
                return False
            else:
                return True
        if exists_piece and board.board[i][j].color == color:
            return True
        i += x_pos
        j += y_pos
        exists_piece = board.board[i][j] != None

    return True


def check_diag(board, start, to):
    """
    Checks if there are no pieces along the diagonal path from
    `start` (non-inclusive) to `to` (non-inclusive). 
    board : Board
        Representation of the current board
    start : tup
        Start location of diagonal path
    to : tup
        End location of diagonal path
    """

    if abs(start[0] - to[0]) != abs(start[1] - to[1]):
        print(incorrect_path)
        return False

    x_pos =  1 if to[0] - start[0] > 0 else -1
    y_pos = 1 if to[1] - start[1] > 0 else -1

    i = start[0] + x_pos
    j = start[1] + y_pos
    while (i < to[0] if x_pos==1 else i > to[0]):
        if board.board[i][j] != None:
            print(blocked_path)
            print("At: " + str((i, j)))
            return False
        i += x_pos
        j += y_pos
    return True


def check_updown_castle(color, board, start, to):
    """
    Checks if there are any threats from the opposite `color` from `start` (non-inclusive)
    to `to` (inclusive) on board `board`.
    color : bool
        True if white's turn
    
    board : Board
        Representation of the current board
    start : tup
        Start location of vertical path
    to : tup
        End location of vertical path
    """
    
    x_pos = 1 if to[0] - start[0] > 0 else -1
    i = start[0] + x_pos

    front_piece = board[i][start[1]]
    if front_piece != None and front_piece.name == 'K' and front_piece.color != color:
        return False

    while (i <= to[0] if x_pos == 1 else i >= to[0]):
        if board.board[i][start[1]] != None and board.board[i][start[1]].color != color:
            if board.board[i][start[1]].name in ['R', 'Q']:
                return False
            else:
                return True
        if board.board[i][start[1]] != None and board.board[i][start[1]].color == color:
            return True
        
    return True

def check_updown(board, start, to):
    """
    Checks if there are no pieces along the vertical or horizontal path
    from `start` (non-inclusive) to `to` (non-inclusive). 
    board : Board
        Representation of the current board
    start : tup
        Start location of diagonal path
    to : tup
        End location of diagonal path
    """
    if start[0] == to[0]:
        smaller_y = start[1] if start[1] < to[1] else to[1]
        bigger_y = start[1] if start[1] > to[1] else to[1]

        for i in range(smaller_y + 1, bigger_y):
            if board.board[start[0]][i] != None:
                print(blocked_path)
                print("At: " + str(start[0], i))
                return False
        return True
    else:
        smaller_x = start[0] if start[0] < to[0] else to[0]
        bigger_x = start[0] if start[0] > to[0] else to[0]

        for i in range(smaller_x + 1, bigger_x):
            if board.board[i][start[1]] != None:
                print(blocked_path)
                return False
        return True



class Piece():
    """
    A class to represent a piece in chess
    
    ...
    Attributes:
    -----------
    name : str
        Represents the name of a piece as following - 
        Pawn -> P
        Rook -> R
        Knight -> N
        Bishop -> B
        Queen -> Q
        King -> K
    color : bool
        True if piece is white
    Methods:
    --------
    is_valid_move(board, start, to) -> bool
        Returns True if moving the piece at `start` to `to` is a legal
        move on board `board`
        Precondition: [start] and [to] are valid coordinates on the board.board
    is_white() -> bool
        Return True if piece is white
    """
    def __init__(self, color):
        self.name = ""
        self.color = color

    def is_valid_move(self, board, start, to):
        return False

    def is_white(self):
        return self.color

    def __str__(self):
        if self.color:
            return self.name
        else:
            return '\033[94m' + self.name + '\033[0m'

class Rook(Piece):
    def __init__(self, color, first_move = True):
        """
        Same as base class Piece, except `first_move` is used to check
        if this rook can castle.
        """
        super().__init__(color)
        self.name = "R"
        self.first_move = first_move 

    def is_valid_move(self, board, start, to):
        if start[0] == to[0] or start[1] == to[1]:
            return check_updown(board, start, to)
        print(incorrect_path)
        return False

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "N"

    def is_valid_move(self, board, start, to):
        if abs(start[0] - to[0]) == 2 and abs(start[1] - to[1]) == 1:
            return True
        if abs(start[0] - to[0]) == 1 and abs(start[1] - to[1]) == 2:
            return True
        print(incorrect_path)
        return False

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "B"

    def is_valid_move(self, board, start, to):
        return check_diag(board, start, to)

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "Q"

    def is_valid_move(self, board, start, to):
        # diagonal
        if abs(start[0] - to[0]) == abs(start[1] - to[1]):
            return check_diag(board, start, to)

        # up/down
        elif start[0] == to[0] or start[1] == to[1]:
            return check_updown(board, start, to)
        print(incorrect_path)
        return False

class King(Piece):
    def __init__(self, color, first_move = True):
        """
        Same as base class Piece, except `first_move` is used to check
        if this king can castle.
        """
        super().__init__(color)
        self.name = "K"
        self.first_move = first_move 
        
    def can_castle(self, board, start, to, right):
        """
        Returns True if king at `start` can move to `to` on `board`.
        board : Board
            Represents the current board
        start : tup
            Position of the king
        to : tup
            Position of the resulting move
        right: bool
            True if castling to the right False otherwise
        Precondition: moving from `start` to `to` is a castling move
        """

        # White castling to the right
        if self.color and right:
            knight_attack = check_knight(self.color, board, (6, 3)) and \
                check_knight(self.color, board, (6, 4)) and \
                check_knight(self.color, board, (5, 4)) and \
                check_knight(self.color, board, (5, 5)) and \
                check_knight(self.color, board, (5, 6)) and \
                check_knight(self.color, board, (5, 7)) and \
                check_knight(self.color, board, (6, 7))
            if not knight_attack: 
                return False

            diags = check_diag_castle(self.color, board, (7, 5), (2, 0)) and \
                check_diag_castle(self.color, board, (7, 6), (1, 0)) and \
                check_diag_castle(self.color, board, (7, 5), (5, 7)) and \
                check_diag_castle(self.color, board, (7, 6), (6, 7))
            if not diags:
                return False

            updowns = check_updown_castle(self.color, board, (7, 5), (0, 5)) and \
                check_updown_castle(self.color, board, (7, 6), (0, 6))
            if not updowns: 
                return False

            board.board[to[0]][to[1]] = King(True, False) 
            board.board[to[0]][to[1]-1] = Rook(True, False) 
            board.board[start[0]][start[1]] = None
            board.board[7][7] = None
            return True
        
        # White castling to the left
        if self.color and not right:
            knight_attack = check_knight(self.color, board, (6, 0)) and \
                check_knight(self.color, board, (6, 1)) and \
                check_knight(self.color, board, (5, 1)) and \
                check_knight(self.color, board, (5, 2)) and \
                check_knight(self.color, board, (5, 3)) and \
                check_knight(self.color, board, (5, 4)) and \
                check_knight(self.color, board, (6, 4)) and \
                check_knight(self.color, board, (6, 5)) 
            if not knight_attack: 
                return False

            diags = check_diag_castle(self.color, board, (7, 2), (5, 0)) and \
                check_diag_castle(self.color, board, (7, 3), (4, 0)) and \
                check_diag_castle(self.color, board, (7, 2), (2, 7)) and \
                check_diag_castle(self.color, board, (7, 3), (3, 7))
            if not diags:
                return False

            updowns = check_updown_castle(self.color, board, (7, 2), (0, 2)) and \
                check_updown_castle(self.color, board, (7, 3), (0, 3))
            if not updowns: 
                return False
            board.board[to[0]][to[1]] = King(True, False) 
            board.board[to[0]][to[1]+1] = Rook(True, False)
            board.board[start[0]][start[1]] = None
            board.board[7][0] = None

            return True

        # Black castling to the right
        if not self.color and right:
            knight_attack = check_knight(self.color, board, (1, 3)) and \
                check_knight(self.color, board, (1, 4)) and \
                check_knight(self.color, board, (1, 7)) and \
                check_knight(self.color, board, (2, 4)) and \
                check_knight(self.color, board, (2, 5)) and \
                check_knight(self.color, board, (2, 6)) and \
                check_knight(self.color, board, (2, 7))
            if not knight_attack: 
                return False

            diags = check_diag_castle(self.color, board, (0, 5), (5, 0)) and \
                check_diag_castle(self.color, board, (0, 6), (6, 0)) and \
                check_diag_castle(self.color, board, (0, 5), (2, 7)) and \
                check_diag_castle(self.color, board, (0, 6), (1, 7))
            if not diags:
                return False

            updowns = check_updown_castle(self.color, board, (0, 2), (7, 2)) and \
                check_updown_castle(self.color, board, (0, 3), (7, 3))
            if not updowns: 
                return False

            board.board[to[0]][to[1]] = King(False, False)
            board.board[to[0]][to[1]-1] = Rook(False, False) 
            board.board[start[0]][start[1]] = None
            board.board[0][7] = None

            return True
        
        # Black castling to the left
        if not self.color and not right:
            knight_attack = check_knight(self.color, board, (1, 0)) and \
                check_knight(self.color, board, (1, 1)) and \
                check_knight(self.color, board, (1, 4)) and \
                check_knight(self.color, board, (1, 5)) and \
                check_knight(self.color, board, (2, 1)) and \
                check_knight(self.color, board, (2, 2)) and \
                check_knight(self.color, board, (2, 3)) and \
                check_knight(self.color, board, (2, 4)) 
            if not knight_attack: 
                return False

            diags = check_diag_castle(self.color, board, (0, 2), (5, 7)) and \
                check_diag_castle(self.color, board, (0, 3), (4, 7)) and \
                check_diag_castle(self.color, board, (0, 2), (2, 0)) and \
                check_diag_castle(self.color, board, (0, 3), (3, 0))
            if not diags:
                return False

            updowns = check_updown_castle(self.color, board, (0, 2), (7, 2)) and \
                check_updown_castle(self.color, board, (0, 3), (7, 3))
            if not updowns: 
                return False

            board.board[to[0]][to[1]] = King(False, False)
            board.board[to[0]][to[1]+1] = Rook(False, False) 
            board.board[start[0]][start[1]] = None
            board.board[0][0] = None

            return True


    def is_valid_move(self, board, start, to):
        if self.first_move and abs(start[1] - to[1]) == 2 and start[0] - to[0] == 0:
            return self.can_castle(board, start, to, to[1] - start[1] > 0)

        if abs(start[0] - to[0]) == 1 or start[0] - to[0] == 0:
            if start[1] - to[1] == 0 or abs(start[1] - to[1]) == 1:
                self.first_move = False
                return True

        print(incorrect_path)
        return False


class GhostPawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "GP"

    def is_valid_move(self, board, start, to):
        return False

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "P"
        self.first_move = True

    def is_valid_move(self, board, start, to):
        if self.color:
            # diagonal move
            if start[0] == to[0] + 1 and (start[1] == to[1] + 1 or start[1] == to[1] - 1):
                if board.board[to[0]][to[1]] != None:
                    self.first_move = False
                    return True
                print("Cannot move diagonally unless taking.")
                return False

            # vertical move
            if start[1] == to[1]:
                if (start[0] - to[0] == 2 and self.first_move) or (start[0] - to[0] == 1):
                    for i in range(start[0] - 1, to[0] - 1, -1):
                        if board.board[i][start[1]] != None:
                            print(blocked_path)
                            return False
                    # insert a GhostPawn
                    if start[0] - to[0] == 2:
                        board.board[start[0] - 1][start[1]] = GhostPawn(self.color)
                        board.white_ghost_piece = (start[0] - 1, start[1])
                    self.first_move = False
                    return True
                print("Invalid move" + " or " + "Cannot move forward twice if not first move.")
                return False
            print(incorrect_path)
            return False

        else:
            if start[0] == to[0] - 1 and (start[1] == to[1] - 1 or start[1] == to[1] + 1):
                if board.board[to[0]][to[1]] != None:
                    self.first_move = False
                    return True
                print(blocked_path)
                return False
            if start[1] == to[1]:
                if (to[0] - start[0] == 2 and self.first_move) or (to[0] - start[0] == 1):
                    for i in range(start[0] + 1, to[0] + 1):
                        if board.board[i][start[1]] != None:
                            print(blocked_path)
                            return False
                    # insert a GhostPawn
                    if to[0] - start[0] == 2:
                        board.board[start[0] + 1][start[1]] = GhostPawn(self.color)
                        board.black_ghost_piece = (start[0] + 1, start[1])
                    self.first_move = False
                    return True
                print("Invalid move" + " or " + "Cannot move forward twice if not first move.")
                return False
            print(incorrect_path)
            return False

########################################################################################
# chess.py

import board
import piece

class Chess():
    """
    A class to represent the game of chess.
    
    ...
    Attributes:
    -----------
    board : Board
        represents the chess board of the game
    turn : bool
        True if white's turn
    white_ghost_piece : tup
        The coordinates of a white ghost piece representing a takeable pawn for en passant
    black_ghost_piece : tup
        The coordinates of a black ghost piece representing a takeable pawn for en passant
    Methods:
    --------
    promote(pos:stup) -> None
        Promotes a pawn that has reached the other side to another, or the same, piece
    move(start:tup, to:tup) -> None
        Moves the piece at `start` to `to` if possible. Otherwise, does nothing.
    """

    def __init__(self):
        self.board = board.Board()

        self.turn = True

        self.white_ghost_piece = None
        self.black_ghost_piece = None

    def promotion(self, pos):
        pawn = None
        while pawn == None:
            promote = input("Promote pawn to [Q, R, N, B, P(or nothing)]: ")
            if promote not in ['Q', 'R', 'N', 'B', 'P', '']:
                print("Not a valid promotion piece")
            else:
                if promote == 'Q':
                    pawn = piece.Queen(True)
                elif promote == 'R':
                    pawn = piece.Rook(True)
                elif promote == 'N':
                    pawn = piece.Knight(True)
                elif promote == 'B':
                    pawn = piece.Bishop(True)
                elif promote == 'P' or promote == '': 
                    pawn = piece.Pawn(True)
        self.board.board[pos[0]][pos[1]] = pawn 

    def move(self, start, to):
        """
        Moves a piece at `start` to `to`. Does nothing if there is no piece at the starting point.
        Does nothing if the piece at `start` belongs to the wrong color for the current turn.
        Does nothing if moving the piece from `start` to `to` is not a valid move.
        start : tup
            Position of a piece to be moved
        to : tup
            Position of where the piece is to be moved
        
        precondition: `start` and `to` are valid positions on the board
        """

        if self.board.board[start[0]][start[1]] == None:
            print("There is no piece to move at the start place")
            return

        target_piece = self.board.board[start[0]][start[1]]
        if self.turn != target_piece.color:
            print("That's not your piece to move")
            return

        end_piece = self.board.board[to[0]][to[1]]
        is_end_piece = end_piece != None

        # Checks if a player's own piece is at the `to` coordinate
        if is_end_piece and self.board.board[start[0]][start[1]].color == end_piece.color:
            print("There's a piece in the path.")
            return

        if target_piece.is_valid_move(self.board, start, to):
            # Special check for if the move is castling
            # Board reconfiguration is handled in Piece
            if target_piece.name == 'K' and abs(start[1] - to[1]) == 2:
                print("castled")
                
                if self.turn and self.black_ghost_piece:
                    self.board.board[self.black_ghost_piece[0]][self.black_ghost_piece[1]] = None
                elif not self.turn and self.white_ghost_piece:
                    self.board.board[self.white_ghost_piece[0]][self.white_ghost_piece[1]] = None
                self.turn = not self.turn
                return
                
            if self.board.board[to[0]][to[1]]:
                print(str(self.board.board[to[0]][to[1]]) + " taken.")
                # Special logic for ghost piece, deletes the actual pawn that is not in the `to`
                # coordinate from en passant
                if self.board.board[to[0]][to[1]].name == "GP":
                    if self.turn:
                        self.board.board[
                            self.black_ghost_piece[0] + 1
                        ][
                            self.black_ghost_piece[1]
                        ] = None
                        self.black_ghost_piece = None
                    else:
                        self.board.board[self.white_ghost_piece[0] - 1][self.black_ghost_piece[1]] = None
                        self.white_ghost_piece = None

            self.board.board[to[0]][to[1]] = target_piece
            self.board.board[start[0]][start[1]] = None
            print(str(target_piece) + " moved.")

            if self.turn and self.black_ghost_piece:
                self.board.board[self.black_ghost_piece[0]][self.black_ghost_piece[1]] = None
            elif not self.turn and self.white_ghost_piece:
                self.board.board[self.white_ghost_piece[0]][self.white_ghost_piece[1]] = None

            self.turn = not self.turn


def translate(s):
    """
    Translates traditional board coordinates of chess into list indices
    """
    try:
        row = int(s[0])
        col = s[1]
        if row < 1 or row > 8:
            print(s[0] + "is not in the range from 1 - 8")
            return None
        if col < 'a' or col > 'h':
            print(s[1] + "is not in the range from a - h")
            return None
        dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        return (8 - row, dict[col])
    except:
        print(s + "is not in the format '[number][letter]'")
        return None



if __name__ == "__main__":
    chess = Chess()
    chess.board.print_board()

    while True:
        start = input("From: ")
        to = input("To: ")
        
        start = translate(start)
        to = translate(to)

        if start == None or to == None:
            continue

        chess.move(start, to)

        # check for promotion pawns
        i = 0
        while i < 8:
            if not chess.turn and chess.board.board[0][i] != None and \
                chess.board.board[0][i].name == 'P':
                chess.promotion((0, i))
                break
            elif chess.turn and chess.board.board[7][i] != None and \
                chess.board.board[7][i].name == 'P':
                chess.promotion((7, i))
                break
            i += 1

        chess.board.print_board()

