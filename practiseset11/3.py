try:
    a=int(input("enter any number:"))
    b=int(input("enter any number:"))
    print(a/b)
except ZeroDivisionError as z:
    print("infinite")
    

    