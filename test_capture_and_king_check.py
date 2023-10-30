import unittest
from main import ChessBoard
from chestPieces import Rook, Pawn, King, Bishop, Queen, Knight

class Test_Capture(unittest.TestCase):
    """
    Tests isValidMove() and movePiece() from testing plan.
    Alternates player, uses different moves for each capture test.
    """
    def setUp(self):
        """This method is called before each test."""
        self.board = ChessBoard()
        self.pawn = Pawn("RED") # Assuming "RED" is for white pieces
        self.bishop = Bishop("RED")
        self.queen = Queen("RED")
        self.rook = Rook("BLUE")
        self.knight = Knight("BLUE")
        self.king = King("BLUE")

    # 1. Tests isValidMove() and movePiece() for Pawn
    def test_pawn_capture(self): 
        self.pawn.position = (2, 3)  # Place pawn at D3
        self.board.board[2][3] = self.pawn
        self.rook.position = (3, 2)  # Place enemy rook at C4
        self.board.board[3][2] = self.rook
        self.bishop.position = (3, 4)  # Place friend bishop at E4
        self.board.board[3][4] = self.bishop
        self.king.position = (3,3)
        self.board.board[3][3] = self.king
        #print(self.board.display()) #print the board to verify correct positions
        # Test pawn cannot capture own piece
        self.assertFalse(self.board.isValidMove(self.pawn.position, self.bishop.position))
        # Test pawn can capture enemy piece
        self.assertTrue(self.board.isValidMove(self.pawn.position, self.rook.position))
        # Test pawn vertical capture
        self.assertFalse(self.board.isValidMove(self.pawn.position, self.king.position))
        # Test pawn capture
        self.board.movePiece(self.pawn.position, self.rook.position)
        chesspiece = self.board.board[self.rook.position[0]][self.rook.position[1]]
        self.assertTrue(chesspiece == self.pawn)
        
    # 2. Tests isValidMove() and movePiece() for Rook
    def test_rook_capture(self):
        self.board.switch_player()
        self.rook.position = (2,3) # Place rook at D3
        self.board.board[2][3] = self.rook
        self.queen.position = (5,3) # Place enemy queen at D6
        self.board.board[5][3] = self.queen
        self.knight.position = (2,7) # Place friend knight at H3
        self.board.board[2][7] = self.knight

        # Test rook cannot capture own piece
        self.assertFalse(self.board.isValidMove(self.rook.position, self.knight.position))
        # Test rook can capture enemy piece
        self.assertTrue(self.board.isValidMove(self.rook.position, self.queen.position))
        # Test rook capture
        self.board.movePiece(self.rook.position, self.queen.position)
        chesspiece = self.board.board[self.queen.position[0]][self.queen.position[1]]
        self.assertTrue(chesspiece == self.rook)
        
    def test_bishop_capture(self):
        self.bishop.position = (2, 3)  # Place bishop at D3
        self.board.board[2][3] = self.bishop
        self.knight.position = (5, 6)  # Place enemy knight at G6
        self.board.board[5][6] = self.knight
        self.pawn.position = (4, 1)  # Place friend pawn at B5
        self.board.board[4][1] = self.pawn
        
        # Test bishop cannot capture own piece
        self.assertFalse(self.board.isValidMove(self.bishop.position, self.pawn.position))
        # Test bishop can capture enemy piece
        self.assertTrue(self.board.isValidMove(self.bishop.position, self.knight.position))
        # Test bishop capture
        self.board.movePiece(self.bishop.position, self.knight.position)
        chesspiece = self.board.board[self.knight.position[0]][self.knight.position[1]]
        self.assertTrue(chesspiece == self.bishop)
        
    def test_knight_capture(self):
        self.board.switch_player()
        self.knight.position = (2,3) # Place knight at D3
        self.board.board[2][3] = self.knight
        self.pawn.position = (4,4) # Place enemy pawn at E5
        self.board.board[4][4] = self.pawn
        self.king.position = (3,1) # Place friend king at B4
        self.board.board[3][1] = self.king
        
        # Test knight cannot capture own piece
        self.assertFalse(self.board.isValidMove(self.knight.position, self.king.position))
        # Test knight can capture enemy piece
        self.assertTrue(self.board.isValidMove(self.knight.position, self.pawn.position))
        # Test knight capture
        self.board.movePiece(self.knight.position, self.pawn.position)
        chesspiece = self.board.board[self.pawn.position[0]][self.pawn.position[1]]
        self.assertTrue(chesspiece == self.knight)
        
    def test_queen_capture(self):
        self.queen.position = (2, 3)  # Place queen at D3
        self.board.board[2][3] = self.queen
        self.rook.position = (3, 2)  # Place enemy rook at C4
        self.board.board[3][2] = self.rook
        self.bishop.position = (2, 0)  # Place friend bishop at A3
        self.board.board[2][0] = self.bishop
        
        # Test queen cannot capture own piece
        self.assertFalse(self.board.isValidMove(self.queen.position, self.bishop.position))
        # Test queen can capture enemy piece
        self.assertTrue(self.board.isValidMove(self.queen.position, self.rook.position))
        # Test queen capture
        self.board.movePiece(self.queen.position, self.rook.position)
        chesspiece = self.board.board[self.rook.position[0]][self.rook.position[1]]
        self.assertTrue(chesspiece == self.queen)
        
    def test_king_capture(self):
        self.board.switch_player()
        self.king.position = (2,3) # Place king at D3
        self.board.board[2][3] = self.king
        self.bishop.position = (2,4) # Place enemy bishop at E3
        self.board.board[2][4] = self.bishop
        self.rook.position = (2,2) # Place friend rook at C3
        self.board.board[2][2] = self.rook

        # Test king cannot capture own piece
        self.assertFalse(self.board.isValidMove(self.king.position, self.rook.position))
        # Test king can capture enemy piece
        self.assertTrue(self.board.isValidMove(self.king.position, self.bishop.position))
        # Test king capture
        self.board.movePiece(self.king.position, self.bishop.position)
        chesspiece = self.board.board[self.bishop.position[0]][self.bishop.position[1]]
        self.assertTrue(chesspiece == self.king)
        
class Test_King_Check(unittest.TestCase):
    """
    Tests is_in_check() from testing plan.
    Alternates player, tests for various types of check.
    """
    def setUp(self):
        """This method is called before each test."""
        self.board = ChessBoard()
        #board automatically creates BlueKing and RedKing.
        self.bishop = Bishop("RED")
        self.queen = Queen("RED")
        
        self.rook = Rook("BLUE")
        self.knight = Knight("BLUE")
    
    def test_game_start_check(self):
        self.assertFalse(self.board.is_in_check("RED"))
        self.assertFalse(self.board.is_in_check("BLUE"))
    
    def test_enemy_capture_check(self):
        self.board.switch_player()
        self.board.RedKing.position = (2,3) # Place RedKing at D3
        self.board.board[2][3] = self.board.RedKing
        self.rook.position = (4,3) # Place enemy rook at D5
        self.board.board[4][3] = self.rook
        self.queen.position = (3,3) # Place friend queen at D4
        self.board.board[3][3] = self.queen

        #Enemy rook captures queen to place king in check
        self.board.movePiece(self.rook.position, self.queen.position)
        self.assertTrue(self.board.is_in_check("RED"))
        self.assertFalse(self.board.is_in_check("BLUE"))
        
    def test_friend_capture_check(self):
        self.board.BlueKing.position = (5,5) # Place BlueKing at F6
        self.board.board[5][5] = self.board.BlueKing
        self.bishop.position = (2,2) # Place enemy bishop at C3
        self.board.board[2][2] = self.bishop
        self.knight.position = (3,3) # Place friend knight at E5
        self.board.board[3][3] = self.knight
        
        #Friend knight moves to place king in check
        self.board.movePiece(self.knight.position, (4,5))
        self.assertTrue(self.board.is_in_check("BLUE"))
        self.assertFalse(self.board.is_in_check("RED"))
        
    def test_king_moves_check(self):
        self.board.RedKing.position = (2,3) # Place RedKing at D3
        self.board.board[2][3] = self.board.RedKing
        self.rook.position = (4,3) # Place enemy rook at D5
        self.board.board[4][3] = self.rook
        self.knight.position = (3,3) # Place enemy knight at D4
        self.board.board[3][3] = self.knight
        
        #RedKing captures Knight, placing RedKing in check
        self.board.movePiece(self.board.RedKing.position, self.knight.position)
        self.assertFalse(self.board.is_in_check("BLUE"))
        self.assertTrue(self.board.is_in_check("RED"))
        
    def test_two_check(self):
        self.board.RedKing.position = (2,3) # Place RedKing at D3
        self.board.board[2][3] = self.board.RedKing
        self.rook.position = (4,4) # Place enemy rook at E5
        self.board.board[4][4] = self.rook
        self.knight.position = (3,6) # Place enemy knight at G4
        self.board.board[3][6] = self.knight
        
        self.board.movePiece(self.board.RedKing.position, (3,4))
        self.assertFalse(self.board.is_in_check("BLUE"))
        self.assertTrue(self.board.is_in_check("RED"))
        
    def test_double_check(self):
        self.board.BlueKing.position = (2,3) # Place BlueKing at D3
        self.board.board[2][3] = self.board.BlueKing
        self.knight.position = (3,3) # Place redknight at D4
        self.board.board[3][3] = self.knight
        self.queen.position = (5,3) # Place bluequeen at D6
        self.board.board[5][3] = self.queen
        self.board.RedKing.position = (3,7) # Place RedKing at H4
        self.board.board[3][7] = self.board.RedKing
        
        self.board.movePiece(self.knight.position, (4,5))
        self.assertTrue(self.board.is_in_check("BLUE"))
        self.assertTrue(self.board.is_in_check("RED"))
        
if __name__ == "__main__":
    unittest.main()
