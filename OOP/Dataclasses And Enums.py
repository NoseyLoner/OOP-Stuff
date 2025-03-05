from dataclasses import dataclass
from pydantic import BaseModel
from enum import Enum

# class Bow:
#     def __init__(self,Name,Price,Damage):
#         self.Name = Name
#         self.Price = Price
#         self.Damage = Damage

# BowA = Bow("Great Bow",100,20)
# print(BowA.__dict__)

# @dataclass(frozen = True,order = True,repr = False) 
# class Bow:
#     Name: str
#     Price: float
#     damage: int

# Bow1 = Bow("Great Bow",99.99,20)
# Bow2 = Bow("Great Bow","exspensive",20)

# print(Bow2)

# class Bow(BaseModel):
#     Name: str
#     Price: float
#     Damage: int

# Bow1 = Bow(Name = "Great Bow",Price = 99.99,Damage = 20)
# print(Bow1.Damage)

class Weapons(Enum):
    Sword = "Sword"
    Bow = "Bow"
    Axe = "Axe"

Bow = Weapons("Bow")
print(Bow)

class Armory(BaseModel):
    room: int
    weapons: list[Weapons]

armory = Armory(room = 3)