class Player:
    def __init__(self,HP):
        self.HP = HP

    def walk(self):
        print("I am walking")

class Wizard(Player):
    
    def walk(self):
        print("I am floating...")

class Archer(Player):

    def __init__(self,HP,Arrows):
        super().__init__(HP = HP)
        self.Arrows = Arrows


    def shoot(self):
        self.Arrows -= 1
        print(f"Archer shoots,{self.Arrows} arrows left.")

# Wizard = Wizard(50)
# Wizard.walk()

# Archer = Archer(100,5)
# Archer.shoot()
# print(Archer.HP)

# X = {"Test":123}
# print(X)
# X["Test"] = 200
# print(X)

class NoUpdateDictionary(dict):
    def __setitem__(self,Key,Value):
        if Key in self:
            raise KeyError("Key already present")
        super().__setitem__(Key,Value)

Y = NoUpdateDictionary()
Y["key"] = 123
Y["key"] = 123
print(Y)