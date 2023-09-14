from chessPieceADT import ChessPiece

class Pawn(ChessPiece):
    def __init__(self,team):
        self.name = 'p'
        if team == 1: self.name = self.name.upper()
        self.move_vector = [None,None]
        self.position = [None,None]

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

class King(ChessPiece):
    def __init__(self,team):
        self.name = 'k'
        if team == 1: self.name = self.name.upper()
        self.move_vector = 2*[]
        self.position = 2*[]

class Bishop(ChessPiece):
    def __init__(self,team):
        self.name = 'b'
        if team == 1: self.name = self.name.upper()
        self.move_vector = 2*[]
        self.position = 2*[]


