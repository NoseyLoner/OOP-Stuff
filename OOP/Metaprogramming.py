class MetaClass(type):

    def __call__(self,*args,**kwds):
        print("__call__")
        return super().__call__(*args, **kwds)
    
    @classmethod
    def __prepare__(metacls, name, bases,**kwds):
        print("__prepare__")
        return {"HP":100,"Mana":100}
    
    def __new__(metacls,name,bases,namespace):
        print("__new__")
        print(namespace)
        return super().__new__(metacls,name,bases,namespace)

class SingleTon(type):
    _Instance = {}

    def __call__(cls,*args,**kwds):
        print("__call__ in singleton")
        if not cls in cls._Instance:
            cls._Instance[cls] = super().__call__(*args,**kwds)
        return cls._Instance[cls]

class Archer(metaclass = SingleTon):

    def __init__(self,HP):
        self.HP = HP

test = Archer(50)
test2 = Archer(540)

print(id(test))
print(id(test2))



