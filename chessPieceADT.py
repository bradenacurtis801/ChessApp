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

    # @abstractmethod
    #def isValidMove(self, dest_row: int, dest_col: int) -> bool:
        """
        Check if moving to the given destination row and column is valid for this piece.
        Return True if valid, otherwise return False.
        """
    #    pass
        

        
