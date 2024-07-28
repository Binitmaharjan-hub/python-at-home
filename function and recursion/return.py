def work():
    n = input("Enter your job: ")
    if n.isalpha():
        print("nice")
    else:
        return "error"

result = work()
if result:
    print(result)
