from abc import ABC,abstractmethod

class AbstractArcher(ABC):

    @abstractmethod
    def Walk(self):
        print("I Walk...")

    @property
    @abstractmethod
    def HP(self):
        pass

class Archer(AbstractArcher):

    def __init__(self,HP) -> None:
        self._HP = HP
    
    def Walk(self):
        super().Walk()
    
    @property
    def HP(self):
        return self._HP
    
Archer1 = Archer(50)
Archer1.Walk()