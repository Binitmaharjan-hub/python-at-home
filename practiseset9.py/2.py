import math
class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"the square is{self.n**2}")
    def cube(self):
        print(f"the cube is{self.n**3}")
    def squreroot(self):
        print(f"the squareroot is{self.n**1/2}")

a=calculator(4)
a.square()
a.cube()
a.squreroot()