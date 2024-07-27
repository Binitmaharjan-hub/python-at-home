#find greatest among any numbers
x = int(input("Enter any number: "))
y = int(input("Enter any number: "))
z = int(input("Enter any number: "))
a = int(input("Enter any number: "))

# greatest = min(x, y, z, a)
# print(f"The greatest number is: {greatest}")
if x>y and x>z and x>a:
    print(f"x is the greatest {x}")
if y>z and y>x and y>a:
    print(f"y is greatest {y}")
if z>x and z>y and z>a:
    print(f"z is greatest {z}")
if a>x and a>y and a>z:
    print(f"a is greatest {a}")