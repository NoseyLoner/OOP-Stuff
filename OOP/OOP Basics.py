class Archer: # creates a Archer class
    species = "human" # creates a class atribute species that is shared with every object of the class
    
    def __init__(self,hp,mana,arrows): # constuctor method for the Archer class
        self.hp = hp
        self.mana = mana
        self.arrows = arrows

    def shoot(self): # instance method,noted by the "self" argument
        if self.arrows > 0: # checks the number of arrows left
            self.arrows -= 1 # sets "self.arrows" to 1 les than it is 
            print(f"Archer shot,{self.arrows} arrows left")
        else:
            print("Archer cannot shot,no arrows left.")

    @classmethod # a method that is belongs to the class rather than the instance
    def clsmethod(cls,data_string): # defines a class method called "clsmethod" and take argument "data_string"
        hp,mana,arrows = map(int,data_string.split("-")) # uses the map function with an iteratable to asign values to hp,mana and arrows 
        return cls(hp,mana,arrows) # returns hp,mana and arrows
    
    @staticmethod # used for methods that object/classes can use but don't need the self/cls data 
    def static(): # defines static with no arguments
        print("I am static")


archer1 = Archer(100,100,3) # creates a archer object called "archer1"
archer2 = Archer.clsmethod("100-100-5") # calls the Archer class method "clsmethod" to create "archer2",mimicing an __init__ method
archer2.static() # calls static on archer2 

