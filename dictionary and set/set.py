#set only contains values
#set is used where elements cannot be repeated
e=set()#empty set
print(type(e))
s1={1,2,3,4,5,6,6,6}
s2={6,7,8,9,0,2}
# sum=s1.add(777)
# s1.remove(6)
print(s1.union(s2))
print(s1.intersection(s2))
