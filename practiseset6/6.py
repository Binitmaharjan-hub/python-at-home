x=float(input("enter the marks of students:"))
if x==100 and x>=90:
    print("excellent")
elif x<90 and x>=80:
    print("A")
elif x<80 and x>=70:
    print("B+")
elif x<70 and x>=60:
    print("B")
else:
    print("fail")