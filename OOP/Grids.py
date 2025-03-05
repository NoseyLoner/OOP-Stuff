import typing

class Grid:
    def __init__(self,Dimensions:tuple[int,int],Left = False,Top = False,Right = False,Back = False):
        self.Dimension = Dimensions
        self.Grid = []
        self.Entities = {}
        self.Left = Left
        self.Top = Top
        self.Right = Right
        self.Back = Back
        for i in range(Dimensions[1]):
            self.Grid.append([])
            for j in range(Dimensions[0]):
                self.Grid[i].append("[     ]")  # Initialize with "[     ]"
    
    def Display(self):
        for i in range(len(self.Grid)):
            for j in range(len(self.Grid[i])):
                if (j,i) in self.Entities:  # Check if there's an entity at this position
                    self.Grid[i][j] = f"[  {self.Entities[(j,i)]}  ]" # Replace "[     ]" with the entity representation
                # if self.Left:
                #     if self.Dimension[1] %  2 == 0:
                #         self.Grid[1][self.Dimension[0] // 2] = f"[ -> ]"
                #     else:
                #         self.Grid[1][self.Dimension[0] // 2] = f"[ -> ]"
                #         self.Grid[1][self.Dimension[0] // 2 + 1] = f"[ -> ]"
                print(self.Grid[i][j], end="")
            print("\n", end="")
    
    def __add__(self, Other):
        self.Entities[Other.Position] = Other
        return self

class Tester:

    def __init__(self,Position,Repr):
        self.Position = Position
        self.Repr = Repr
    
    def __repr__(self):
        return self.Repr


# Test = Grid((5, 4),Left = True)
# Test.Display()
# OtherTest = Tester((2, 3),"X")
# C1 = Tester((0,0),"1")
# Test = Test + C1
# Test = Test + OtherTest
# print()
# Test.Display()
