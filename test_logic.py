import unittest
from main import ChessBoard
from chestPieces import Rook, Pawn
class TestLogic(unittest.TestCase):

    def setUp(self):
        """This method is called before each test."""
        self.board = ChessBoard()
        
    
    #Tests [EC15] from testing plan: isValidMove
    def test_valid_rook_move(self):
        # Clear the pawn in front of the rook
        self.board.board[1][0] = None
        # Test a valid move for a RED rook
        src_coord = self.board.convert_to_coord("A1")
        dest_coord = self.board.convert_to_coord("A5")
        valid_move = self.board.isValidMove(src_coord, dest_coord)
        self.assertTrue(valid_move, "Rook should be able to move vertically.")

    #Tests [EC16] from testing plan: isValidMove
    def test_invalid_pawn_move(self):
        # Test an invalid move for a RED pawn
        src_coord = self.board.convert_to_coord("B7")
        dest_coord = self.board.convert_to_coord("C6")
        invalid_move = self.board.isValidMove(src_coord, dest_coord)
        self.assertFalse(invalid_move, "Pawn should not be able to move diagonally unless capturing.")


    #Tests [EC1] [EC2] from testing plan.
    def test_validate_input(self):
        # Test valid inputs
        self.assertTrue(self.board.validateInput('H8-H7'))

        # Test invalid inputs
        self.assertFalse(self.board.validateInput('A1A2'))  # Missing '-'


    #TODO: test capture
    #TODO: test check
    
    #TODO: test board boundaries

if __name__ == "__main__":
    unittest.main()


      
        