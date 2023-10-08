from abc import ABC, abstractmethod

class ChessPiece(ABC):

    def __init__(self):
        self.move_vector = [None,None]
        self.position = [None,None]
        self.points = None
     
    # @abstractmethod   
    def getPos(self):
        return self.position
    
    # @abstractmethod
    def setPos(self, row: int, col: int):
        self.position = [row, col]
    
    # @abstractmethod
    def getMoveVector(self):
        pass

 
        

        
