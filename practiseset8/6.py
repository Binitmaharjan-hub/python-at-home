def convert_inches_to_centimeter(inches):
    return (inches*2.54)
inche=int(input("enter inches:"))
centimeter=convert_inches_to_centimeter(inche)
print(f"{inche}={centimeter}")
