from abc import ABC, abstractmethod

class ChessPiece(ABC):

    def __init__(self):
        self.move_vector = [None,None]
        self.position = [None,None]
        self.points = None
     
    # @abstractmethod   
    def getPos(self):
        pass
    
    # @abstractmethod
    def setPos(self, row: int, col: int):
        pass
    
    # @abstractmethod
    def getMoveVector(self):
        pass
        

        
