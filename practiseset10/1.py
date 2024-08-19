class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"the vector of 2d is {self.i}i +{self.j}j")
class treeDvector(twoDvector):
    def __init__(self,i,j,k) :
        super().__init__(i, j)
        self.k=k
    def show(self):
         print(f"the vector of 3d isP{self.i}i +{self.j}j +{self.k}k")

a=twoDvector(2,3)
a.show()
b=treeDvector(1,2,3)
b.show()
        
