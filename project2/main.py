#perfect guess
import random
x=random.randint(1,1000)
guesses=0
z=-1
print(x)
while x !=z:
    z=int(input("enter the number you gussed:"))
    if z<x:
        print("higher number please")
        guesses +=1
    elif(z>x):
        print("lower number please")
        guesses +=1

print(f"you have guessed the correct number {x} in {guesses} guess")