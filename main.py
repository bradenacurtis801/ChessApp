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

class ChessBoard:
    
    def __init__(self):
        self.board = [
            [Rook('Black'), Knight('Black'), Bishop('Black'), Queen('Black'), King('Black'), Bishop('Black'), Knight('Black'), Rook('Black')],
            [Pawn('Black'), Pawn('Black'), Pawn('Black'), Pawn('Black'), Pawn('Black'), Pawn('Black'), Pawn('Black'), Pawn('Black')],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Pawn('White'), Pawn('White'), Pawn('White'), Pawn('White'), Pawn('White'), Pawn('White'), Pawn('White'), Pawn('White')],
            [Rook('White'), Knight('White'), Bishop('White'), Queen('White'), King('White'), Bishop('White'), Knight('White'), Rook('White')]
        ]
        # Setting the initial positions of the pieces
        for row in range(8):
            for col in range(8):
                if self.board[row][col]:
                    self.board[row][col].position = (row, col)
        self.current_player = "White"

    def display(self):
        for i, row in enumerate(self.board, start=1):
            display_row = []
            for piece in row:
                display_row.append(piece.__class__.__name__[0] if piece else ' ')
            print(f"{9-i} | " + ' | '.join(display_row) + ' |')
            print("---------------------------------")
        print("    A   B   C   D   E   F   G   H")

    def get_coordinates(self, command):
        source, destination = command.split('-')
        source = (8-int(source[1]), ord(source[0].upper())-65)
        destination = (8-int(destination[1]), ord(destination[0].upper())-65)
        return source, destination

            

if __name__ == "__main__":
    game = ChessBoard()
    game.play()
