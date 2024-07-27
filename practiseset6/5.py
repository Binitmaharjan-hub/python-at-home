party_list=[]
while (True):
    y=input("enter the name of people you want to invite(press exit):")
    if y == "exit":
        break
    name=party_list.append(y)
print("list of members: ")
for x in party_list:
    print(x)
    
while True:
    z=input("enter the name of guest:")
    if z=="exit":
        break
    if z in party_list:
        print("is in list")
    else:
        print("not in list")

