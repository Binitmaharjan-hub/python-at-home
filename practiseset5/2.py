# s=set()
# num1=(input("enter any number:"))
# s.add (int(num1))
# num2=(input("enter any number:"))
# s.add (int(num2))
# num3=(input("enter any number:"))
# s.add (int(num3))
# num4=(input("enter any number:"))
# s.add (int(num4))
# num5=(input("enter any number:"))
# s.add (int(num5))
# num6=(input("enter any number:"))
# s.add (int(num6))
# print(s)
s=set()
for x in range(6):
    num=int(input("enter number:"))
    s.add(num)
print(s)