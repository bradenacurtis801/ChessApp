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
        self.assertFalse(self.king.validateMove((6,6), self.board.board))
        #test two squares away
        self.assertTrue(self.king.validateMove((3,5), self.board.board))

    def test_rook_movement(self):
        self.rook.position = (4, 4)
        self.board.board[4][4] = self.rook
        # Test vertical and horizontal movement
        self.assertTrue(self.rook.validateMove((4, 6), self.board.board))
        self.assertTrue(self.rook.validateMove((6, 6), self.board.board))
        # Test diagonal movement (this should be False)
        self.assertFalse(self.rook.validateMove((7, 7), self.board.board))

    def test_pawn_promotion(self):
        self.pawn.team = 0
        self.pawn.position = (6, 7)
        self.board.board[6][7] = self.pawn
        # Simulate a move to H8 (promotion rank for white pawns)
        dest_cord = (7, 7)
        self.board.handle_promotion(dest_cord)
        # Check if the piece at H8 is a Queen and belongs to white team
        promoted_piece = self.board.board[7][7]
        self.assertIsInstance(promoted_piece, Queen, "Pawn was not promoted to a Queen.")
        self.assertEqual(promoted_piece.team, 'BLUE', "Promoted piece is not of the expected team.")

    def test_knight_movement(self):
        self.knight.position = (4, 4)  # Place the knight at E5
        self.board.board[4][4] = self.knight
        # Test the L-shaped movements
        # 2 squares up and 1 square right
        self.assertTrue(self.knight.validateMove((2, 5), self.board.board))
        # 2 squares up and 1 square left
        self.assertTrue(self.knight.validateMove((2, 3), self.board.board))
        # 1 square up and 2 squares right
        self.assertTrue(self.knight.validateMove((3, 6), self.board.board))
        # 1 square up and 2 squares left
        self.assertTrue(self.knight.validateMove((3, 2), self.board.board))
        # 2 squares down and 1 square right

        #TODO: test pawn
        #TODO: test board boundaries
        #TODO: test capture
        #TODO: test check
        #TODO: test checkmate

if __name__ == "__main__":
    unittest.main()
