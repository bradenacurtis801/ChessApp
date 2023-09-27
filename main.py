from chestPieces import Rook, Pawn, King, Bishop, Queen, Knight
from chessPieceADT import ChessPiece
import sys,os
import pickle
import re

class ChessBoard:
    #Used to print piece captured
    piece_names = {
    'k': 'King',
    'q': 'Queen',
    'r': 'Rook',
    'b': 'Bishop',
    'n': 'Knight',
    'p': 'Pawn'
}

    """Represents a chessboard and handles game operations such as moves and display."""
    def __init__(self):
        """Initialize the chessboard with the default setup."""
        # Standard starting positions for a chess game.
        self.player1 = True
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
        for i, row in enumerate(reversed(self.board)):
            display_row = []
            for piece in row:
                display_row.append(piece.name if piece else ' ')
            print(f"{8-i} | " + ' | '.join(display_row) + ' |')
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
        while True:
            if self.player1:
                player = 'White'
            else:
                player = 'Black'
            resp = input(f'{player}\'s move:')

            if resp == "quit":
                self.quit()
            elif resp == "save":
                self.save()
            elif self.validateInput(resp):

                if self.handleMove(resp):  # Only toggle player if handleMove returns True
                    self.display()
                    self.player1 = not self.player1 # This changes the player move after the current player makes a move
            else:
                print("Invalid input. Please provide a move in the format 'E2 – E4'.")

            
    def handleMove(self, move: str):
        """Parse the move input and handles the move on the board."""
        #get coordinates
        source, destination = [x.strip() for x in move.split('-')]
        source_coord = self.convert_to_coord(source)
        destination_coord = self.convert_to_coord(destination)
        
        # TODO: Use the coordinates to move the piece from source to destination in self.board
        # ...
        if self.isValidMove(source_coord,destination_coord):
            self.movePiece(source_coord, destination_coord)
            return True
        else:
            print("Move was invalid, try again.")
            return False
        
        
    def isValidMove(self,src_cord,dest_cord):
        """Check if the move from src_cord to dest_cord is valid according to chess rules."""
        # TODO
        srcObj = self.board[src_cord[0]][src_cord[1]]
        destObj = self.board[dest_cord[0]][dest_cord[1]]

         # Check if there's a piece at the source coordinate
        if not srcObj:
            print("There's no piece at the source coordinate!")
            return False

        # Check if the piece being moved belongs to the current player
        if ((self.player1 == True and srcObj.name.upper()) or self.player1 == False and srcObj.name.islower()):
            print("You can only move your own pieces!")
            return False
        
        # Check if the destination has a piece of the same player to stop from capturing players own piece
        if destObj:
            if self.player1 and destObj.name.isupper():
                print("You cannot capture your own piece!")
                return False
            elif not self.player1 and destObj.name.islower():
                print("You cannot capture your own piece!")
                return False

        #If there's a piece at the source coordinat, call its isValidMove
        if srcObj:
            return srcObj.validateMove(dest_cord, self.board)
        return False

    
    def movePiece(self, src_cord, dest_cord):
        """Move the piece from the source coordinates to the destination coordinates."""
        #Setting to type ChessPiece to remove 'any' type like 'piece_to_move.setPos' ...
        piece_to_move: ChessPiece = self.board[src_cord[0]][src_cord[1]]
        captured_piece: ChessPiece = self.board[dest_cord[0]][dest_cord[1]]
        
        # Update the board
        self.board[dest_cord[0]][dest_cord[1]] = piece_to_move
        self.board[src_cord[0]][src_cord[1]] = None
        # Update the position attribute of the moved piece 
        piece_to_move.setPos(dest_cord[0], dest_cord[1])
      
        # If there's a piece at the destination square, it's captured. 
        if captured_piece:
            # Use the dictionary to get the full name of the captured piece.
            captured_name = ChessBoard.piece_names[captured_piece.name.lower()]
            print(f"{captured_name} was captured!")

            # Check if the captured piece is a king
            if captured_piece.name.lower() == 'k':
                winning_player = 1 if self.player1 else 2
                print(f"Player {winning_player} wins! The king has been captured.")
                # Here you can either exit the game or offer to restart
                choice = input("Do you want to play again? (yes/no): ").strip().lower()
                if choice == 'yes':
                    self.reset()
                else:
                    self.quit()
    
    def convert_to_coord(self, notation: str):
        """Convert the user-friendly notation (like 'E2') to board coordinates (like (1, 4))."""
        col_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        col = int(col_map[notation[0].upper()])
        row = int(notation[1]) - 1  # 8 - row number to get 0-indexed row
        #type is a tuple, row is flipped because the board is flipped.
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
