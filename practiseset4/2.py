marks=[]
while (True):
    students_marks=input("enter the marks of student (exit for exitting):")
    if students_marks=="exit":
        break
    marks.append(students_marks)

print("the marks of student are:")
for mark in marks:
    print(mark)
