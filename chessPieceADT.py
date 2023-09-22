from abc import ABC, abstractmethod

class ChessPiece(ABC):

    def __init__(self):
        self.position = (None,None)
        self.points = None
        self.team = 0
     
    # @abstractmethod   
    def getPos(self):
        pass
    
    # @abstractmethod
    def setPos(self, pos):
        pass
    
    # @abstractmethod
    def getMoveVector(self):
        pass
    
    def validateMove(self, dest_cord, board):
        pass
