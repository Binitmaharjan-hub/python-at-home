l=[5,6,7,10,15,11]
def numdivisible(n):
    if n%5==0:
        return True
    return False
f=list(filter(numdivisible,l))
print(f)
