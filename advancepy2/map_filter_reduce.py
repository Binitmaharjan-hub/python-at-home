from functools import reduce
l=[3,4,5,6,7,8,9]
s=lambda x:x+x
smap=map(s,l)
print(list(smap))
# filter
def odd(x):
    if x%2!=0:
        return True
    else:

        return False
onlyodd=filter(odd,l)

print(f"the number is {list(onlyodd)}")
# reduce
def sub(a,b):
    return a-b
print (reduce(sub,l))

