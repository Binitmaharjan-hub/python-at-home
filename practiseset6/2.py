# marks_list = []
# for _ in range(3):
#     mark = float(input("Enter the marks: "))
#     marks_list.append(mark)

# for mark in marks_list:
#     if mark > 40 and mark > 33:
#         print("Pass")
#     else:
#         print("Fail")
marks1=int(input("enter the marks:"))
marks2=int(input("enter the marks:"))
marks3=int(input("enter the marks:"))
total_percent=(100)*(marks1+marks2+marks3)/300
if total_percent>=40:
    print("you have pass",total_percent)
else:
    print("you have failed",total_percent)