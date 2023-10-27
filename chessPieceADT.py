from abc import ABC, abstractmethod

class ChessPiece(ABC):

    def __init__(self, team):
        self.name = None
        self.team = team
        self.position = []
        self.points = None

    def getPos(self):
        return self.position

    def setPos(self, row: int, col: int):
        self.position = [row, col]

    @abstractmethod
    def validateMove(self, dest_cord, board):
        """Check if moving to the given destination is valid."""
        pass

    @abstractmethod
    def generateMoves(self, board):
        """Generate all possible moves for the piece from its current position."""
        pass
