import unittest
from main import ChessBoard, BLUE
from chestPieces import Rook, Pawn
class TestLogic(unittest.TestCase):

    def setUp(self):
        """This method is called before each test."""
        self.board = ChessBoard()
        
    """
    isValidMove tests 1-8. Tests [EC15] [EC16] [BP1] from testing plan
    """
    # 1. No piece at source.
    def test_no_piece_at_source(self):
        src = (3, 3)  # Empty square
        dest = (4, 4)
        self.assertFalse(self.board.isValidMove(src, dest))

    # 2. Piece at source but belongs to the opponent.
    def test_move_opponents_piece(self):
        src = (6, 0)  # Blue pawn
        dest = (5, 0)
        self.assertFalse(self.board.isValidMove(src, dest))

    # 3. Piece at source, belongs to the player, but destination has a piece of the same player.
    def test_move_to_own_piece(self):
        src = (1, 0)  # Red pawn
        dest = (0, 0)  # Red rook
        self.assertFalse(self.board.isValidMove(src, dest))

    # 4. Piece at source, belongs to the player, destination is empty, but the move is invalid according to the piece's rules.
    def test_invalid_piece_move_empty_dest(self):
        src = (1, 0)  # Red pawn
        dest = (4, 0)  # Three steps forward, which is invalid
        self.assertFalse(self.board.isValidMove(src, dest))

    # 5. Piece at source, belongs to the player, destination has an opponent's piece, but the move is invalid according to the piece's rules.
    def test_invalid_piece_move_opponent_dest(self):
        src = (1, 0)  # Red pawn
        dest = (6, 0)  # Blue pawn's position
        self.assertFalse(self.board.isValidMove(src, dest))

    # 6. Piece at source, belongs to the player, destination is empty, and the move is valid.
    def test_valid_piece_move_empty_dest(self):
        src = (1, 0)  # Red pawn
        dest = (3, 0)  # Two steps forward
        self.assertTrue(self.board.isValidMove(src, dest))

    # 7. Piece at source, belongs to the player, destination has an opponent's piece, and the move is valid.
    def test_valid_piece_move_opponent_dest(self):

        src = (1, 6)  # Red pawn
        dest = (2, 7)  # Diagonal position, potentially occupied by a Blue piece
        
        # Place a Blue pawn at the destination
        self.board.board[dest[0]][dest[1]] = Pawn(BLUE)

        self.assertTrue(self.board.isValidMove(src, dest))


    # 8. Piece at source, belongs to the player, destination has an opponent's piece, the move is valid, but the piece's validateMove method returns False.
    def test_valid_move_but_validateMove_returns_false(self):
        src = (1, 7)  # Red pawn
        dest = (6, 7)  # Blue pawn's position
      
        self.assertFalse(self.board.isValidMove(src, dest))



    # 9. Tests [EC1] [EC2] from testing plan.  
    def test_validate_input(self):
        # Test valid inputs
        self.assertTrue(self.board.validateInput('H8-H7'))

        # Test invalid inputs
        self.assertFalse(self.board.validateInput('A1A2'))  # Missing '-'


    #TODO: test capture
    #TODO: test check
    #TODO: test board boundaries
    #TODO:  

if __name__ == "__main__":
    unittest.main()


      
        