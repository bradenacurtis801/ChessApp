from chessPieceADT import ChessPiece

class Pawn(ChessPiece):
    def __init__(self, team):
        self.name = 'Pawn'
        self.team = team
        self.position = []
        self.first_move = True
        self.isPromoted = False
        
    def getPos(self):
        return self.position

    def setPos(self, row: int, col: int):
        self.position = [row, col]
        
        if self.first_move:
            self.first_move = False

        # Check if the pawn has reached the end of the board for promotion.
        if self.team == 'RED' and row == 0:
            self.isPromoted = True
        elif self.team == 'BLUE' and row == 7:
            self.isPromoted = True

    def validateMove(self, dest_cord, board):
        moves = self.generateMoves(board)
        if dest_cord in moves:
            # print(f"{self.name} at position {convert_to_human_readable(self.position)} can move to {convert_to_human_readable(dest_cord)}") ## FOR DEBUGGING 
            return True
        return False

    def generateMoves(self, board):
        row = self.position[0]
        col = self.position[1]
        moves = []

        if self.team == 'BLUE':  # Team 1 (RED)
            # Standard move forward
            if self.is_valid_position(row-1, col) and board[row - 1][col] == None:
                moves.append((row - 1, col))
            # First move: can move two spaces forward
            if self.first_move and board[row - 1][col] == None and board[row - 2][col] == None:
                moves.append((row - 2, col))
            # Capture diagonally left
            if self.is_valid_position(row-1, col-1) and board[row - 1][col - 1] and board[row - 1][col - 1].team == 'RED':
                moves.append((row - 1, col - 1))
            # Capture diagonally right
            if self.is_valid_position(row-1, col+1) and board[row - 1][col + 1] and board[row - 1][col + 1].team == 'RED':
                moves.append((row - 1, col + 1))
        else:  # Team 2 (RED)
            # Standard move forward
            if self.is_valid_position(row+1, col) and board[row + 1][col] == None:
                moves.append((row + 1, col))
            # First move: can move two spaces forward
            if self.first_move and board[row + 1][col] == None and board[row + 2][col] == None:
                moves.append((row + 2, col))
            # Capture diagonally left
            if self.is_valid_position(row+1, col-1) and board[row + 1][col - 1] and board[row + 1][col - 1].team == 'BLUE':
                moves.append((row + 1, col - 1))
            # Capture diagonally right
            if self.is_valid_position(row+1, col+1) and board[row + 1][col + 1] and board[row + 1][col + 1].team == 'BLUE':
                moves.append((row + 1, col + 1))

        # print_valid_moves(self.name, self.position, moves) ## FOR DEBUGGING 
        return moves

    def is_valid_position(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8


        
class Rook(ChessPiece):
    def __init__(self, team):
        self.name = 'Rook'
        self.team = team
        self.position = []

    def setPos(self, row: int, col: int):
        self.position = [row, col]

    def validateMove(self, dest_cord, board) -> bool:
        moves = self.generateMoves(board)
        return dest_cord in moves

    def generateMoves(self, board):
        row, col = self.position
        moves = []

        # Check horizontal and vertical directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                srcObj = board[r][c]
                if srcObj is None:
                    moves.append((r, c))
                elif srcObj.team != self.team:
                    moves.append((r, c))
                    break  # Stop if there's an opposing piece (capture)
                else:
                    break  # Stop if there's a friendly piece
                r += dr
                c += dc
        # print_valid_moves(self.name, self.position, moves) ## FOR DEBUGGING 
        return moves

    


class Knight(ChessPiece):
    def __init__(self, team):
        self.name = 'Knight'
        self.team = team
        self.position = []

    def setPos(self, row: int, col: int):
        self.position = [row, col]

    def validateMove(self, dest_cord, board):
        moves = self.generateMoves(board)
        return dest_cord in moves

    def generateMoves(self, board):
        row, col = self.position
        moves = []
        
        # Define the possible relative moves for a knight
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1), 
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for move in knight_moves:
            r, c = row + move[0], col + move[1]
            if 0 <= r < 8 and 0 <= c < 8:
                srcObj = board[r][c]
                if srcObj is None or srcObj.team != self.team:
                    moves.append((r, c))
        # print_valid_moves(self.name, self.position, moves) ## FOR DEBUGGING 
        return moves




class Queen(ChessPiece):
    def __init__(self, team):
        self.name = 'Queen'
        self.team = team
        self.position = []

    def setPos(self, row: int, col: int):
        self.position = [row, col]

    def validateMove(self, dest_cord, board):
        moves = self.generateMoves(board)
        return dest_cord in moves

    def generateMoves(self, board):
        moves = []

        # Horizontal and Vertical moves
        for i in range(8):
            if i != self.position[0]:  # Vertical
                moves.append((i, self.position[1]))
            if i != self.position[1]:  # Horizontal
                moves.append((self.position[0], i))
        
        # Diagonal moves
        for i in [-1, 1]:
            for j in [-1, 1]:
                row, col = self.position[0] + i, self.position[1] + j
                while 0 <= row < 8 and 0 <= col < 8:
                    if board[row][col]:
                        if board[row][col].team != self.team:
                            moves.append((row, col))
                        break
                    else:
                        moves.append((row, col))
                    row += i
                    col += j
        # print_valid_moves(self.name, self.position, moves) ## FOR DEBUGGING 
        return moves




class King(ChessPiece):
    def __init__(self, team):
        self.name = 'King'
        self.team = team
        self.position = []

    def setPos(self, row: int, col: int):
        self.position = [row, col]

    def validateMove(self, dest_cord, board):
        moves = self.generateMoves(board)
        return dest_cord in moves

    def generateMoves(self, board):
        moves = []
        row, col = self.position
        # Check all squares around the king
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row = row + i
                new_col = col + j
                # Ensure it's a valid position on the board
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    srcObj = board[new_row][new_col]
                    if srcObj is None:
                        moves.append((new_row, new_col))
                    elif srcObj.team != self.team:
                        moves.append((new_row, new_col))
        return moves


class Bishop(ChessPiece):
    def __init__(self, team):
        self.name = 'Bishop'
        self.team = team
        self.position = []

    def setPos(self, row: int, col: int):
        self.position = [row, col]

    def validateMove(self, dest_cord, board):
        moves = self.generateMoves(board)
        return dest_cord in moves

    def generateMoves(self, board):
        moves = []
        for i in [-1, 1]:
            for j in [-1, 1]:
                row, col = self.position[0] + i, self.position[1] + j
                while 0 <= row < 8 and 0 <= col < 8:
                    if board[row][col]:
                        if board[row][col].team != self.team:
                            moves.append((row, col))
                        break
                    else:
                        moves.append((row, col))
                    row += i
                    col += j
        return moves



#### TEMP FOR DEBUGGING USE#####
def convert_to_human_readable(coord):
    row_to_num = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8'}
    col_to_letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
    
    row, col = coord
    return col_to_letter[col] + row_to_num[row]


def print_valid_moves(piece_name, position, moves):
    human_readable_position = convert_to_human_readable(position)
    human_readable_moves = [convert_to_human_readable(move) for move in moves]
    print(f"Valid moves for {piece_name} at {human_readable_position}: {', '.join(human_readable_moves)}")
