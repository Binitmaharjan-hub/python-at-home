# #list created from user inputs

# fruits=[]
# f1=input("enter any fruit:")
# fruits.append(f1)
# f2=input("enter any fruit:")
# fruits.append(f2)
# f3=input("enter any fruit:")
# fruits.append(f3)
# f4=input("enter any fruit:")
# fruits.append(f4)
# print(fruits)
# Initialize an empty list to store the foods
food_list = []

# Loop to continuously take user input until they decide to stop
while True:
    # Ask the user to enter a food item
    food_item = input("Enter a food item (or type 'done' to finish): ")
    
    # Check if the user wants to finish inputting food items
    if food_item == 'done':
        break
    
    # Add the food item to the list
    food_list.append(food_item)

# Print the final list of food items
print("Your list of food items:")
for food in food_list:
    print(food)

