from chestPieces import Rook, Pawn, King, Bishop, Queen, Knight
import sys,os
import pickle
import re

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
        
    def validateInput(self, move):
        return re.match(r'^[A-Ha-h][1-8]\s*-\s*[A-Ha-h][1-8]$', move, re.I)
            
    def run(self):
        player1 = True
        while True:
            if player1:
                player = 1
            else:
                player = 2
            resp = input(f'Player {player} turn:')

            if resp == "quit":
                self.quit()
            elif resp == "save":
                self.save()
            elif self.validateInput(resp):
                self.handleMove(resp)
                self.display()
            else:
                print("Invalid input. Please provide a move in the format 'E2 – E4'.")

            # This changes the player move after the current player makes a move
            player1 = not player1
            
    def handleMove(self, move):
        # implemented but needs to be tested
        source, destination = [x.strip() for x in move.split('-')]
        source_coord = self.convert_to_coord(source)
        destination_coord = self.convert_to_coord(destination)
        
        # TODO: Use the coordinates to move the piece from source to destination in self.board
        # ...
        self.isValidMove(source_coord,destination_coord)
        
    def isValidMove(self,src_cord,dest_cord):
        # TODO
        srcObj = self.board[src_cord[0]][src_cord[1]]
        destObj = self.board[dest_cord[0]][dest_cord[1]]
        pass
    
    def convert_to_coord(self, notation):
        col_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        col = col_map[notation[0].upper()]
        row = 8 - int(notation[1])  # 8 - row number to get 0-indexed row
        return (row, col)
                
            
    def quit(self):
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print a friendly exit message
        print("Thanks for playing! Goodbye!")
        # Exit the program
        sys.exit()
        
    def save(self):
        # implemented but needs to be tested
        print("Optional TODO: this saves the same state")
        with open("chess_save.dat", "wb") as f:
            pickle.dump(self, f)
        print("Game has been saved!")
        
    @classmethod
    def load(cls):
        # implemented but needs to be tested
        try:
            with open("chess_save.dat", "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("No saved game found.")
            return None

    
    def reset(self):
        self.__init__()
        self.run()


            

if __name__ == "__main__":
    print("Welcome to Chess!")
    choice = input("Do you want to load a saved game? (yes/no): ").strip().lower()

    if choice == 'yes':
        game = ChessBoard.load()
        if game:
            game.run()
        else:
            print("Starting a new game.")
            game = ChessBoard()
            game.run()
    else:
        game = ChessBoard()
        game.run()
