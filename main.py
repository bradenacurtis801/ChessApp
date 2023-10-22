from chestPieces import Rook, Pawn, King, Bishop, Queen, Knight
from chessPieceADT import ChessPiece
import sys
import os
import pickle
import re
import json

BLUE = "BLUE"  # White is now Blue
RED = "RED"  # Black is now Red

COLORS = {
    'BLUE': '\033[94m',  # Blue color
    'RED': '\033[91m',  # Red color
    'ENDC': '\033[0m'     # Reset to default
}


class ChessBoard:
    # Used to print piece captured
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
        self.BlueKing = King("BLUE")
        self.RedKing = King("RED")
        self.player1 = True  # Red team starts first

        # Functions to initialize rows
        def init_pawns(team):
            return [Pawn(team) for _ in range(8)]

        def init_majors(team):
            return [Rook(team), Knight(team), Bishop(team), Queen(team), 
                    self.BlueKing if team == "BLUE" else self.RedKing, 
                    Bishop(team), Knight(team), Rook(team)]
        # Setting up the board
        self.board = [
            init_majors("RED"),
            init_pawns("RED"),
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            init_pawns("BLUE"),
            init_majors("BLUE")
        ]

        # Setting the initial positions of the pieces
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    piece.position = (row, col)

    def display(self):
        uniDict = {
            BLUE: {Pawn: "♙", Rook: "♖", Knight: "♘", Bishop: "♗", King: "♔", Queen: "♕"},
            RED: {Pawn: "♟", Rook: "♜", Knight: "♞",
                  Bishop: "♝", King: "♚", Queen: "♛"}
        }
        """Display the current state of the chessboard."""
        for i, row in enumerate(reversed(self.board), start=1):
            display_row = []
            for piece in row:
                if piece:
                    color = COLORS[piece.team]
                    symbol = uniDict[piece.team][type(piece)]
                    display_row.append(color + symbol + COLORS['ENDC'])
                else:
                    display_row.append(' ')
            print(f"{9-i} | " + ' | '.join(display_row) + ' |')
            print("---------------------------------")
        print("    A   B   C   D   E   F   G   H")

    def validateInput(self, move):
        return re.match(r'^[A-Ha-h][1-8]\s*-\s*[A-Ha-h][1-8]$', move, re.I)

    def run(self):
        """Main game loop, handles input from the players and game progression."""
        self.display()
        while True:
            if self.player1:
                player = 'Blue'
            else:
                player = 'Red'
            resp = input(f'{player}\'s move:')

            if resp == "quit":
                self.quit()
            elif self.validateInput(resp):
                if self.handleMove(resp):
                    self.display()
            else:
                print("Invalid input. Please provide a move in the format 'E2 – E4'.")

    def switch_player(self):
        """Switch the active player."""
        self.player1 = not self.player1

    def handleMove(self, move):
        """Parse the move input and handles the move on the board."""
        source, destination = [x.strip() for x in move.split('-')]
        source_coord = self.convert_to_coord(source)
        destination_coord = self.convert_to_coord(destination)

        # TODO: Use the coordinates to move the piece from source to destination in self.board
        # ...
        if self.isValidMove(source_coord, destination_coord):
            self.movePiece(source_coord, destination_coord)
            # self.display() ### placed here for debugging purposes
            self.switch_player()
            opponent_team = 'RED' if self.player1 else 'BLUE'
            if self.is_in_check(opponent_team):
                print(f"Check! It's {opponent_team}'s turn.")
            return True
        else:
            print("Move was invalid, try again.")
            return False

    def isValidMove(self, src_cord, dest_cord):
        """Check if the move from src_cord to dest_cord is valid according to chess rules."""

        srcObj = self.board[src_cord[0]][src_cord[1]]
        destObj = self.board[dest_cord[0]][dest_cord[1]]

        # Check if there's a piece at the source coordinate
        if not srcObj:
            print("There's no piece at the source coordinate!")
            return False

        # Check if the piece being moved belongs to the current player
        if self.player1 and srcObj.team == RED:
            pass
        elif not self.player1 and srcObj.team == BLUE:
            pass
        else:
            print("You can only move your own pieces!")
            return False

        # Check if the destination has a piece of the same player to stop from capturing players own piece
        if destObj:
            if self.player1 and destObj.team == RED:
                print("You cannot capture your own piece!")
                return False
            elif not self.player1 and destObj.team == BLUE:
                print("You cannot capture your own piece!")
                return False

        # If there's a piece at the source coordinate, call its isValidMove
        if srcObj:
            return srcObj.validateMove(dest_cord, self.board)
        return False

    def movePiece(self, src_cord, dest_cord):
        """Move the piece from the source coordinates to the destination coordinates."""
        piece_to_move: ChessPiece = self.board[src_cord[0]][src_cord[1]]
        captured_piece: ChessPiece = self.board[dest_cord[0]][dest_cord[1]]

        # Update the board
        self.board[dest_cord[0]][dest_cord[1]] = piece_to_move
        self.board[src_cord[0]][src_cord[1]] = None

        # Update the position attribute of the moved piece
        piece_to_move.setPos(dest_cord[0], dest_cord[1])

        if isinstance(piece_to_move, Pawn) and piece_to_move.isPromoted:
            promoted_queen = Queen(piece_to_move.team)
            promoted_queen.setPos(dest_cord[0], dest_cord[1])
            self.board[dest_cord[0]][dest_cord[1]] = promoted_queen

        # If there's a piece at the destination square, it's captured.
        if captured_piece:
            captured_name = captured_piece.name
            print(f"{captured_name} was captured!")

            # Check if the captured piece is a king
            if captured_name.lower() == 'king':
                winning_player = 'Red' if self.player1 else 'Blue'
                print(
                    f"Player {winning_player} wins! The king has been captured.")
                # Here you can either exit the game or offer to restart
                choice = input(
                    "Do you want to play again? (yes/no): ").strip().lower()
                if choice == 'yes':
                    self.reset()
                else:
                    self.quit()

    def is_in_check(self, team):
        # Get the king's position based on the team.
        king_pos = self.BlueKing.position if team == 'BLUE' else self.RedKing.position
        print(f"Checking for team {team}. King's position: {king_pos}")

        # Check if any opposing pieces can attack the king.
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece and piece.team != team:
                    if piece.validateMove(tuple(king_pos), self.board):
                        attacker_name = piece.name
                        print(
                            f"{attacker_name} at position {(i, j)} can attack the king at {king_pos}")
                        return True
        return False

    def convert_to_coord(self, notation):
        """Convert the user-friendly notation (like 'E2') to board coordinates (like (1, 4))."""
        col_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                'E': 4, 'F': 5, 'G': 6, 'H': 7}
        col = col_map[notation[0].upper()]
        row = int(notation[1]) - 1  # Adjusted to match the new board orientation
        # type is a tuple, row is flipped because the board is flipped.
        return (row, col)


    def quit(self):
        """Quit the game, clearing the console and printing an exit message."""
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print a friendly exit message
        print("Thanks for playing! Goodbye!")
        # Exit the program
        sys.exit()

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
