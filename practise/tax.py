income=int(input("enter your monthly income:"))
yearly=income*12
if yearly<=500000:
    tax=(5/100*500000)
    income_after_tax=yearly-tax
elif yearly<=1000000:
    tax=500000*0.05+(yearly-500000)*0.10
    income_after_tax=yearly-tax

else:
    tax=500000*0.05+1000000*0.10+(yearly-1000000)*0.25
    income_after_tax=yearly-tax

print(income_after_tax)