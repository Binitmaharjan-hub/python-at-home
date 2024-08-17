students_dict = {}

while True:
    name = input("Enter the name of the student (or type 'exit' to stop): ")
    if name.lower() == 'exit':
        break
    age = int(input("Enter the age of the student: "))
    
    students_dict[name] = age
total_age=sum (students_dict.values())
print(total_age)


        


