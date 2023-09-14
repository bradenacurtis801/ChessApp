from abc import ABC, abstractmethod

class ChessPiece(ABC):

    def __init__(self, team):
        self.team = team
        self.move_vector = 2*[]
        self.position = 2*[]
     
    @abstractmethod   
    def getPos(self):
        pass
    
    @abstractmethod
    def setPos(self, row: int, col: int):
        pass
    
    @abstractmethod
    def getMoveVector(self):
        pass
        

        
