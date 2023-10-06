from chessPieceADT import ChessPiece

class Pawn(ChessPiece):
    def __init__(self,team):
        self.name = 'p'
        self.team = team
        if self.team == 0: self.name = self.name.upper()
        self.position = []
        
    def getPos(self):
        return self.position
    
    def setPos(self, newPos):
        self.position = newPos
        
    def validateMove(self, dest_cord, board):
        print("pawn validatemove entered!")
        #generate possible moves
        row = self.position[0]
        col = self.position[1]
        moves = []
        print(self.team)
        if self.team == 0:
            srcObj = board[row+1][col]
            if srcObj == None:
                moves.append((row+1, col))
            #TODO add checking for front corners and for out of bounds
                srcObj2 = board[row+2][col]
                if row == 1 and srcObj2 == None:
                    moves.append((row+2,col))
        #TODO add check for opposite side pawn
        print(dest_cord)
        if dest_cord in moves:
            return True
        return False

class Rook(ChessPiece):
    def __init__(self, team):
        self.name = 'r'
        self.team = team
        if self.team == 0: self.name = self.name.upper()
        self.position = []

    def getPos(self):
        return self.position

    def setPos(self, newPos):
        self.position = newPos

    def validateMove(self, dest_cord, board):
        print("rook validatemove entered!")
        row, col = self.position
        dest_row, dest_col = dest_cord
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

        print(dest_cord)
        return dest_cord in moves


class Knight(ChessPiece):
    def __init__(self, team):
        self.name = 'n'
        self.team = team
        if self.team == 0: self.name = self.name.upper()
        self.position = []

    def getPos(self):
        return self.position

    def setPos(self, newPos):
        self.position = newPos

    def validateMove(self, dest_cord, board):
        print("knight validatemove entered!")
        row, col = self.position
        moves = []
        # Define the possible moves for a knight
        knight_moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Check if the destination is within the board and not occupied by a friendly piece
        for move in knight_moves:
            r, c = move
            if 0 <= r < 8 and 0 <= c < 8:
                srcObj = board[r][c]
                if srcObj is None or srcObj.team != self.team:
                    moves.append(move)
        print(dest_cord)
        return dest_cord in moves


class Queen(ChessPiece):
    def __init__(self,team):
        self.name = 'q'
        self.team = team
        if self.team == 0: self.name = self.name.upper()
        self.move_vector = 2*[]
        self.position = 2*[]

class King(ChessPiece):
    def __init__(self,team):
        self.name = 'k'
        self.team = team
        if self.team == 0: self.name = self.name.upper()
        self.position = []
    
    def getPos(self):
        return self.position
    
    def setPos(self, newPos):
        self.position = newPos
    
    #a King can move one square in any direction
    def validateMove(self, dest_cord, board):
        #generate possible moves
        row = self.position[0]
        col = self.position[1]
        moves = []
        #check all squares around king (including the king)
        for i in range(-1,2):
            for j in range(-1,2):
                try:
                    srcObj = board[row+i][col+j]
                    if srcObj == None:
                        moves.append((row+i,col+j))
                    else:
                        if srcObj.team != self.team:
                            moves.append((row+i, col+j))
                except IndexError:
                    pass
        #check if the destination is one of the valid moves
        if dest_cord in moves:
            return True
        return False

class Bishop(ChessPiece):
    def __init__(self,team):
        self.name = 'b'
        self.team = team
        if self.team == 0: self.name = self.name.upper()
        self.move_vector = 2*[]
        self.position = 2*[]


