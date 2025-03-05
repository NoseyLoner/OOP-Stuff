# class A:
    
#     def SayHi(self):
#         print("Hello from A")

# class B(A):
    
#     def SayHi(self):
#         print("Hello from B")

# class C(A):
    
#     def SayHi(self):
#         print("Hello from C")

# class D(B,C):
#     pass

# d = D()
# d.SayHi()

import json

class Archer:

    def __init__(self,HP):
        self.HP = HP

    def walk(self):
        return "I am walking"
    
class JsonMixin:
    
    def ToJson(self):
        return json.dumps(self,default = lambda o: o.__dict__)

class SuperWalkMixin:

    def walk(self):
        return f"{super().walk()} extremley fast!"
    
class SuperArcher(JsonMixin,SuperWalkMixin,Archer):
    pass

A = SuperArcher(100)
print(A.walk())
print(A.ToJson())
