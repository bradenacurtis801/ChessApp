from chestPieces import Rook, Pawn, King, Bishop, Queen, Knight

col = {
    'A':0,
    'B':1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7
}

pieces = [
    Rook,
    Pawn,
    King,
    Bishop,
    Queen,
    Knight
]

class ChessBoard:
    def __init__(self):
        self.board = [
            [Rook(0), Knight(0), Bishop(0), Queen(0), King(0), Bishop(0), Knight(0), Rook(0)],
            [Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0), Pawn(0)],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1), Pawn(1)],
            [Rook(1), Knight(1), Bishop(1), Queen(1), King(1), Bishop(1), Knight(1), Rook(1)]
        ]
        # Setting the initial positions of the pieces
        for row in range(8):
             for col in range(8):
                if self.board[row][col]:
                    self.board[row][col].position = (row, col)

    def display(self):
        for i, row in enumerate(self.board, start=1):
            display_row = []
            for piece in row:
                display_row.append(piece.name if piece else ' ')
            print(f"{9-i} | " + ' | '.join(display_row) + ' |')
            print("---------------------------------")
        print("    A   B   C   D   E   F   G   H")

    def get_coordinates(self, command):
        source, destination = command.split('-')
        source = (8-int(source[1]), ord(source[0].upper())-65)
        destination = (8-int(destination[1]), ord(destination[0].upper())-65)
        return source, destination
    
    def initBoard(self):
        for piece,_col in enumerate(pieces):
            newObj = piece().setPos(row=1,col=_col)
            newObj = piece().setPos(row=8,col=_col)


            

if __name__ == "__main__":
    game = ChessBoard()
    game.display()
