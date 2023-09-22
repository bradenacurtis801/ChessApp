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
    def __init__(self,team):
        self.name = 'r'
        self.team = team
        if self.team == 0: self.name = self.name.upper()
        self.move_vector = 2*[]
        self.position = 2*[]

class Knight(ChessPiece):
    def __init__(self,team):
        self.name = 'n'
        self.team = team
        if self.team == 0: self.name = self.name.upper()
        self.move_vector = 2*[]
        self.position = 2*[]

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


