class Employee:
    salary=100000
    increment=10

    @property
    def salaryafterincrement(self):
        return(self.salary+self.salary*(self.increment/100))
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment=((salary/self.salary)-1)*100
e=Employee()
print(e.salaryafterincrement)
e.salaryafterincrement=1010
print(e.increment)


