class Archer:

    def __init__(self,HP):
        self.HP = HP

    def Walk(self):
        return "I Am Walking..."
    
    def Attack(self):
        return "I Shoot An Arrow!"
    
class Knight:
     
    def __init__(self,HP):
        self.HP = HP

    def Walk(self):
        return "I Am Marching..."
    
    def Attack(self):
        return "I Swing My Sword!"
    
def CreateCharacter(self,Type,HP):
    if Type == "Archer":
        return Archer(HP)
    elif Type == "Knight":
        return Knight(HP)
    else:
        raise ValueError("Unknown Character Type")

Archer1 = CreateCharacter("Archer",100)
Knight1 = CreateCharacter("Knight",100)

print(Archer1.Walk())
print(Knight1.Walk())

class AttackStratagy:
     
    def Execute(self):
        pass
     
class BowAttack(AttackStratagy):
     
    def Execute(self):
        return "Shooting A Bow"
    
class CrossbowAttack(AttackStratagy):
     
    def Execute(self):
        return "Shoot With A Crossbow"
     
class Archer:
     
    def __init__(self,HP,Strategy):
        self.HP = HP 
        self.Stategy = Strategy

    def Attack(self):
        return self.Stategy.Execute()

Archer1 = Archer(100,BowAttack())
print(Archer1.Attack())
Archer1.Stategy = CrossbowAttack()
print(Archer1.Attack())

class Observer:

    def Update(self,Subject):
        pass

class King(Observer):

    def __init__(self,Name):
        self.Name = Name

    def Update(self, Subject: Knight):
        print(f"{self.Name} received update from {Subject.__class__.__name__}: New HP is {Subject.HP}")

class Knight:

    def  __init__(self,HP):
        self.HP = HP
        self.Observer = []

    def Attach(self,Observer):
        self.Observer.append(Observer)

    def Notify(self):
        for Observer in self.Observer:
            Observer.Update(self)

    def SetHP(self,HP):
        self.HP = HP
        self.Notify()

Test = Knight(100)
KingArthur = King("King Arthur")
KingRichard = King("King Richard")

Test.Attach(KingArthur) 
Test.Attach(KingRichard)

Test.SetHP(50)
