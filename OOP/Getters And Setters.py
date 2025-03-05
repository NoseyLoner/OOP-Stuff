import time

#  class Archer:
    
#     def __init__(self,HP):
#         self._HP = HP

#     def GetHP(self):
#         print("Getter Called")
#         return self._HP

#     def SetHP(self,Value):
#         if Value > 200:
#             raise ValueError("HP can be 200 at max!")
#         print("Setter Called")
#         self._HP = Value

#     HP = property(GetHP,SetHP)

# Archer1 = Archer(100)
# Archer1.HP = 201
# print(Archer1.HP)

class Archer:
    
    def __init__(self,HP,Damage):
        self._HP = HP
        self._Damage = Damage
        self.Crit = 1.3
        self._OverallDamage = None

    @property
    def Damage(self):
        return self._Damage

    @Damage.setter
    def Damage(self,Value):
        self._Damage = Value
        self._OverallDamage = None
    
    @property
    def OverallDamage(self):
        if self._OverallDamage is None:
            print("Compute...")
            time.sleep(3)
            self._OverallDamage = round(self.Damage * self.Crit,1)
        else:
            print("Using Cache")
        return self._OverallDamage
    
    @OverallDamage.setter
    def OverallDamage(self,Valur):
        raise ValueError("Changing Overall Damage not allowed")

Archer1 = Archer(100,20)
Archer1._Damage = 35
Archer1.OverallDamage = 34