# i=1
# n=int(input("enter any number:"))
# while(i<n):
#     fabo=n+i
#     i=i+1
# print(fabo)
def fabo(n):
    if n==0 or n==1:
        return 1
    else:
        return fabo(n-1)+fabo(n-2)

a=fabo(8)
if a:
    print(a)