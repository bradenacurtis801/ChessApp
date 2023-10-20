import unittest
from main import ChessBoard

from chestPieces import Rook, Pawn, King, Bishop, Queen, Knight


class TestChessPieces(unittest.TestCase):

    def setUp(self):
        """This method is called before each test."""
        self.board = ChessBoard()
        self.queen = Queen(1)  # Assuming 0 is for white pieces
        self.bishop = Bishop(1)
        self.king = King(1)


    def test_queen_valid_move(self):
        self.queen.position = (4, 4)  # Place queen at E5
        self.board.board[4][4] = self.queen
        # Test a valid vertical move
        self.assertTrue(self.queen.validateMove((6, 4), self.board.board))
        # Test a valid horizontal move
        self.assertTrue(self.queen.validateMove((4, 6), self.board.board))
        # Test a valid diagonal move
        self.assertTrue(self.queen.validateMove((6, 6), self.board.board))

    def test_queen_invalid_move(self):
        self.queen.position = (4, 4)  # Place queen at E5
        self.board.board[4][4] = self.queen
        # Test an invalid L-shape move (like a knight)
        self.assertFalse(self.queen.validateMove((6, 5), self.board.board))

    def test_bishop_valid_move(self):
        self.bishop.position = (4, 4)  # Place bishop at E5
        self.board.board[4][4] = self.bishop
        # Test a valid diagonal move
        self.assertTrue(self.bishop.validateMove((6, 6), self.board.board))

    def test_bishop_invalid_move(self):
        self.bishop.position = (4, 4)  # Place bishop at E5
        self.board.board[4][4] = self.bishop
        # Test an invalid vertical move
        self.assertFalse(self.bishop.validateMove((6, 4), self.board.board))

    def test_king_movement(self):
        self.king.position = (4,4)
        self.board.board[4][4] = self.king
        #test vertical, diagonal, and horizontal
        self.assertTrue(self.king.validateMove((5,4), self.board.board))
        self.assertTrue(self.king.validateMove((5,5), self.board.board))
        self.assertTrue(self.king.validateMove((4,5), self.board.board))
        #test two squares away
        self.assertFalse(self.king.validateMove((6,6), self.board.board))

        #TODO: test rook, pawn, knight movement     
        #TODO: test board boundaries
        #TODO: test capture
        #TODO: test check
        #TODO: test checkmate
        
        
if __name__ == "__main__":
    unittest.main()
