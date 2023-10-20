from abc import ABC

class ChessPiece(ABC):
    """Abstract Class which each piece inherits"""
    def __init__(self):
        self.position = [None,None]
        
     
    def getPos(self):
        return self.position

      
    def setPos(self, row: int, col: int):
        self.position = [row, col]
        
