# i=1
# n=int(input("enter a number:"))
# while(i<n):
#     fact=(n*i)
#     i=i+1
# print(fact)
#now by using recursion
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
    
a=fact(3)
if a:
    print(a)
