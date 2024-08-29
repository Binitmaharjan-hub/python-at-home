from functools import reduce
l=[5,6,7,10,15,11]
def maximum(a,b):
    if a>b:
        return a
    return b

r=(reduce(maximum,l))
print(r)

