students_dict = {}

while True:
    try:
        name = input("Enter the name of the student (or type 'exit' to stop): ")
        if not name.isalpha():
            raise ValueError("Name should be a string without numbers.")
    except ValueError as e:
        print("Error:", e)
        continue
    
    if name.lower() == 'exit':
        break

    try:
        age = int(input("Enter the age of the student: "))
    except ValueError:
        print("You cannot use words for age.")
        continue
    
    students_dict[name] = age

print(students_dict)

total_age = sum(students_dict.values())
print("Total age of all students:", total_age)
