from chessPieceADT import ChessPiece

class Pawn(ChessPiece):
    def __init__(self, team):
        self.name = 'p'
        if team == 1: self.name = self.name.upper()
        self.position = [None, None]
        self.first_move = True

    def validateMove(self, dest_cord, board):
        # generate possible moves
        row = self.position[0]
        col = self.position[1]
        moves = []

        if self.name.isupper():  # Team 1 (White)
            # Standard move forward
            if board[row - 1][col] == None:
                moves.append((row - 1, col))
            # First move: can move two spaces forward
            if self.first_move and board[row - 2][col] == None:
                moves.append((row - 2, col))
            # Capture diagonally left
            if col > 0 and board[row - 1][col - 1] and board[row - 1][col - 1].name.islower():
                moves.append((row - 1, col - 1))
            # Capture diagonally right
            if col < 7 and board[row - 1][col + 1] and board[row - 1][col + 1].name.islower():
                moves.append((row - 1, col + 1))

        else:  # Team 2 (Black)
            # Standard move forward
            if board[row + 1][col] == None:
                moves.append((row + 1, col))
            # First move: can move two spaces forward
            if self.first_move and board[row + 2][col] == None:
                moves.append((row + 2, col))
            # Capture diagonally left
            if col > 0 and board[row + 1][col - 1] and board[row + 1][col - 1].name.isupper():
                moves.append((row + 1, col - 1))
            # Capture diagonally right
            if col < 7 and board[row + 1][col + 1] and board[row + 1][col + 1].name.isupper():
                moves.append((row + 1, col + 1))

        if dest_cord in moves:
            self.first_move = False  # After a move, set first_move to False
            return True
        return False

class Rook(ChessPiece):
    def __init__(self,team):
        self.name = 'r'
        if team == 1: self.name = self.name.upper()
        self.move_vector = 2*[]
        self.position = 2*[]

class Knight(ChessPiece):
    def __init__(self,team):
        self.name = 'n'
        if team == 1: self.name = self.name.upper()
        self.move_vector = 2*[]
        self.position = 2*[]

class Queen(ChessPiece):
    def __init__(self,team):
        self.name = 'q'
        if team == 1: self.name = self.name.upper()
        self.move_vector = 2*[]
        self.position = 2*[]
    

    def validateMove(self, dest: tuple, board) -> bool:
        dest_row, dest_col = dest
        # Check for horizontal, vertical, or diagonal movement
        row_diff = abs(dest_row - self.position[0])
        col_diff = abs(dest_col - self.position[1])
        
        # Check for horizontal movement
        if self.position[0] == dest_row:
            return self.is_path_clear_horizontal(dest_col, board)
        # Check for vertical movement
        elif self.position[1] == dest_col:
            return self.is_path_clear_vertical(dest_row , board)
        # Check for diagonal movement
        elif row_diff == col_diff:
            return self.is_path_clear_diagonal(dest_row, dest_col, board)
        return False

    def is_path_clear_horizontal(self, dest_col, board):
        step = 1 if dest_col > self.position[1] else -1
        for col in range(self.position[1] + step, dest_col, step):
            if board[self.position[0]][col]:
                return False
        return True

    def is_path_clear_vertical(self, dest_row, board):
        step = 1 if dest_row > self.position[0] else -1
        for row in range(self.position[0] + step, dest_row, step):
            if board[row][self.position[1]]:
                return False
        return True

    def is_path_clear_diagonal(self, dest_row, dest_col, board):
        row_step = 1 if dest_row > self.position[0] else -1
        col_step = 1 if dest_col > self.position[1] else -1
        row, col = self.position[0] + row_step, self.position[1] + col_step
        while row != dest_row and col != dest_col:
            if board[row][col]:
                return False
            row += row_step
            col += col_step
        return True


class King(ChessPiece):
    def __init__(self, team):
        self.name = 'k'
        if team == 1: self.name = self.name.upper()
        self.position = []
    
    #a King can move one square in any direction
    def validateMove(self, dest_cord, board) -> bool:
        dest_row, dest_col = dest_cord
        # Generate possible moves
        row = self.position[0]
        col = self.position[1]
        moves = []
        # Check all squares around king (including the king)
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    srcObj = board[row + i][col + j]
                    if srcObj == None:
                        moves.append((row + i, col + j))
                    else:
                        if (self.name.isupper() and srcObj.name.islower()) or (self.name.islower() and srcObj.name.isupper()):
                            moves.append((row + i, col + j))
                except IndexError:
                    pass
        # Check if the destination is one of the valid moves
        if dest_cord in moves:
            return True
        return False
    
class Bishop(ChessPiece):
    def __init__(self,team):
        self.name = 'b'
        if team == 1: self.name = self.name.upper()
        self.move_vector = 2*[]
        self.position = 2*[]

    def validateMove(self, dest: tuple, board) -> bool:
        dest_row, dest_col = dest
        # Check for diagonal movement
        row_diff = abs(dest_row - self.position[0])
        col_diff = abs(dest_col - self.position[1])
        
        if row_diff == col_diff:
            return self.is_path_clear_diagonal(dest_row, dest_col, board)
        return False

    def is_path_clear_diagonal(self, dest_row, dest_col, board):
        # Same as the Queen's is_path_clear_diagonal method
        row_step = 1 if dest_row > self.position[0] else -1
        col_step = 1 if dest_col > self.position[1] else -1
        row, col = self.position[0] + row_step, self.position[1] + col_step
        while row != dest_row and col != dest_col:
            if board[row][col]:
                return False
            row += row_step
            col += col_step
        return True