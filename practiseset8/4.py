def sum_of_natural_num(n):
    if n==0 or n==1:
        return 1
    else:
        return (n-1)+n

print("sum =",sum_of_natural_num(2))