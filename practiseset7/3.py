i=int(input("enter any number:"))
for x in range(2,i):
    if i%x ==0:
        print("not prime number")
        break
    else:
        print("prime number")
        break
        