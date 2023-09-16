from chestPieces import Rook, Pawn, King, Bishop, Queen, Knight
import sys,os
import pickle
import re

class ChessBoard:
    """Represents a chessboard and handles game operations such as moves and display."""
    def __init__(self):
        """Initialize the chessboard with the default setup."""
        # Standard starting positions for a chess game.
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
                    
                    
        self.display()

    def display(self):
        """Display the current state of the chessboard."""
        for i, row in enumerate(self.board, start=1):
            display_row = []
            for piece in row:
                display_row.append(piece.name if piece else ' ')
            print(f"{9-i} | " + ' | '.join(display_row) + ' |')
            print("---------------------------------")
        print("    A   B   C   D   E   F   G   H")
        
    def validateInput(self, move):
        """
    Validates the input move string to ensure it matches the pattern of a valid chess move.
    
    A valid move is of the format: 'A1-A2' where 'A1' and 'A2' are coordinates on the chessboard.
    The function allows for case-insensitive input and optional spaces around the hyphen.
    
    Args:
        move (str): The move string to be validated.
    
    Returns:
        MatchObject: Returns a match object if the move is valid, otherwise returns None.
    """
        return re.match(r'^[A-Ha-h][1-8]\s*-\s*[A-Ha-h][1-8]$', move, re.I)

            
    def run(self):
        """Main game loop, handles input from the players and game progression."""
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
        """Parse the move input and handles the move on the board."""
        source, destination = [x.strip() for x in move.split('-')]
        source_coord = self.convert_to_coord(source)
        destination_coord = self.convert_to_coord(destination)
        
        # TODO: Use the coordinates to move the piece from source to destination in self.board
        # ...
        if self.isValidMove(source_coord,destination_coord):
            pass
            #TODO move chest peice
        else:
            print("Move was invalid, try again.")
            player1 = not player1 #prevents current player from changing
            self.run()
        
    def isValidMove(self,src_cord,dest_cord):
        """Check if the move from src_cord to dest_cord is valid according to chess rules."""
        # TODO
        srcObj = self.board[src_cord[0]][src_cord[1]]
        destObj = self.board[dest_cord[0]][dest_cord[1]]
        if srcObj:
            pass
    
    def convert_to_coord(self, notation):
        """Convert the user-friendly notation (like 'E2') to board coordinates (like (1, 4))."""
        col_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        col = col_map[notation[0].upper()]
        row = 8 - int(notation[1])  # 8 - row number to get 0-indexed row
        return (row, col)
                
            
    def quit(self):
        """Quit the game, clearing the console and printing an exit message."""
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print a friendly exit message
        print("Thanks for playing! Goodbye!")
        # Exit the program
        sys.exit()
        
    def save(self):
        """Save the current game state to a file for later continuation."""
        # implemented but needs to be tested
        print("Optional TODO: this saves the same state")
        with open("chess_save.dat", "wb") as f:
            pickle.dump(self, f)
        print("Game has been saved!")
        
    @classmethod
    def load(cls):
        """Load a previously saved game state from a file."""
        # implemented but needs to be tested
        try:
            with open("chess_save.dat", "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("No saved game found.")
            return None

    
    def reset(self):
        """Reset the game state to the default starting position and restarts the game."""
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
