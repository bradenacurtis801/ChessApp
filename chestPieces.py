from chessPieceADT import ChessPiece

class Pawn(ChessPiece):
    def __init__(self):
        self.name = 'p'

class Rook(ChessPiece):
    def __init__(self):
        self.name = 'r'

class Knight(ChessPiece):
    def __init__(self):
        self.name = 'n'

class Queen(ChessPiece):
    def __init__(self):
        self.name = 'q'

class King(ChessPiece):
    def __init__(self):
        self.name = 'k'

class Bishop(ChessPiece):
    def __init__(self):
        self.name = 'b'


