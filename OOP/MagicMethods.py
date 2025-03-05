import uuid

class Archer: # creates a Archer class
    species = "human" # creates a class atribute species that is shared with every object of the class
    
    def __init__(self,hp,mana,arrows): # constuctor method for the Archer class
        self.hp = hp
        self.mana = mana
        self.arrows = arrows
        self._id = uuid.uuid4() 

    def __str__(self):
        return f"Archer with {self.hp} health,{self.mana} mana and {self.arrows} arrows"

    def __repr__(self):
        return f"Archer({self.hp},{self.mana},{self.arrows})"

    def __add__(self,other):
        if not isinstance(other,Archer):
            return NotImplemented
        NewHp = self.hp + other.hp
        NewMana = self.mana + other.mana
        NewArrows = self.arrows + other.arrows
        return Archer(NewHp,NewMana,NewArrows)
    
    def __eq__(self, other):
        if not isinstance(other,Archer):
            return False
        return self.hp == other.hp and self.mana == other.mana and self.arrows == other.arrows
            
    def __gt__(self,other):
        if not isinstance(other,Archer):
            return NotImplemented
        return self.hp > other.hp
    
    def __hash__(self):
        return hash(self._id)

archer1 = Archer(100,100,5)

class Company:
    
    def __init__(self,size):
        self.size = size
        self.archers = []

    def AddArcher(self,arhcer):
        if not isinstance(arhcer,Archer):
            raise TypeError("Only Archers allowed")
        if len(self.archers) > self.size:
            raise ValueError("Company already full")
        self.archers.append(arhcer)

    def __add__(self,other ):
        if not isinstance(other,Archer):
            raise TypeError("Only adding archers allowed")
        self.AddArcher(other)
        return self
    
    def __iter__(self):
        return iter(self.archers) 

archer2 = Archer(100,100,5)
company = Company(5)
newcompany = company + archer2 + archer2 + archer2

for archer in newcompany:
    print(archer)