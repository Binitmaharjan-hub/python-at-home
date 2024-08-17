# class programmer:
#     language="javascript"
#     salary=10000

# binit=programmer()
# programmer.name="binit"
# print(binit.name,binit.language,binit.salary)

# rohan=programmer()
# programmer.name="rohan"
# print(rohan.name,rohan.language,rohan.salary)
class programmer:
    company="google"
    def __init__(self,name,language,salary) :
        self.name=name
        self.language=language
        self.salary=salary

a=programmer("binit","python",10000)
b=programmer("hamal","python",10000)
c=programmer("bishal","python",10000)
print(a.name,a.salary,a.language)
print(b.name,b.salary,b.language)
print(c.name,c.salary,c.language)
        