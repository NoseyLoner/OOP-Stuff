class Deskriptor:

    def __get__(self,Instance,Owner):
        return Instance.__dict__[self.Name]

    def __set__(self,Instance,Value):
        if Value < 0 or Value > 100:
            raise ValueError("Value has to be between 0 and 100")
        Instance.__dict__[self.Name] = Value

    def __set_name__(self,Owner,Name):
        self.Name = Name

class Lifes:

    def __get__(self,Instance,owner):
        return 3

    def __set__(self,Instance,Value):
        pass


class Archer:
    
    HP = Deskriptor
    Mana = Deskriptor
    lifes = Lifes()

    def __init__(self,HP,Mana,Lifes):
        self.HP = HP
        self.Mana = Mana
        self.lifes = Lifes

Archer1 = Archer(100,30,6)
print(Archer1.lifes)
