class Archer:

    __slots__ = ("HP","Mana")

    def __init__(self,HP,Mana):
        self.HP = HP
        self.Mana = Mana 

class SuperArcher(Archer):

    __slots__ = ("Arrows")

    def __init__(self, HP, Mana,Arrows):
        super().__init__(HP, Mana)
        self.Arrows = Arrows

SArcher = SuperArcher(100,50,20)
print(SArcher.__slots__)
