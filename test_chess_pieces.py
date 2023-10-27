import unittest
from main import ChessBoard
from chestPieces import Rook, Pawn, King, Bishop, Queen, Knight

class TestChessPieces(unittest.TestCase):

    def setUp(self):
        """This method is called before each test."""
        self.board = ChessBoard()
        self.queen = Queen(0)  # Assuming 0 is for white pieces
        self.bishop = Bishop(0)
        self.king = King(0)
        self.pawn = Pawn(0)
        self.rook = Rook(0)
        self.knight = Knight(0)

    # Tests [EC8] from testing plan
    def test_queen_valid_move(self): 
        self.queen.position = (4, 4)  # Place queen at E5
        self.board.board[4][4] = self.queen
        # Test a valid vertical move
        self.assertTrue(self.queen.validateMove((6, 4), self.board.board))
        # Test a valid horizontal move
        self.assertTrue(self.queen.validateMove((4, 6), self.board.board))
        # Test a valid diagonal move
        self.assertTrue(self.queen.validateMove((6, 6), self.board.board))

    # Tests [EC9] from testing plan
    def test_queen_invalid_move(self): 
        self.queen.position = (4, 4)  # Place queen at E5
        self.board.board[4][4] = self.queen
        # Test an invalid L-shape move (like a knight)
        self.assertFalse(self.queen.validateMove((6, 5), self.board.board))

    # Tests [EC8] from testing plan
    def test_bishop_valid_move(self):
        self.bishop.position = (4, 4)  # Place bishop at E5
        self.board.board[4][4] = self.bishop
        # Test a valid diagonal move
        self.assertTrue(self.bishop.validateMove((6, 6), self.board.board))

    # Tests [EC9] from testing plan
    def test_bishop_invalid_move(self):
        self.bishop.position = (4, 4)  # Place bishop at E5
        self.board.board[4][4] = self.bishop
        # Test an invalid vertical move
        self.assertFalse(self.bishop.validateMove((6, 4), self.board.board))

    # Tests [EC12][EC13] from testing plan
    def test_king_movement(self):
        self.king.position = (4,4)
        self.board.board[4][4] = self.king
        #test vertical, diagonal, and horizontal
        self.assertTrue(self.king.validateMove((5,4), self.board.board))
        self.assertTrue(self.king.validateMove((5,5), self.board.board))
        self.assertTrue(self.king.validateMove((4,5), self.board.board))
        #test two squares away
        self.assertFalse(self.king.validateMove((6,6), self.board.board))

    def test_rook_movement(self):
        self.rook.position = (4, 4)
        self.board.board[4][4] = self.rook
        #test vertical and horizontal movement
        self.assertTrue(self.rook.validateMove((4,6), self.board.board))
        self.assertTrue(self.rook.validateMove((6, 6), self.board.board))
        #test diagonal movement
        self.assertFalse(self.rook.validateMove((7,7), self.board.board))

        #TODO: test pawn, knight movement     
        #TODO: test board boundaries
        #TODO: test capture
        #TODO: test check
        #TODO: test checkmate

if __name__ == "__main__":
    unittest.main()
