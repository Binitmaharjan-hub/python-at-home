import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def evaluate_expression(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error! {str(e)}"

def trigonometry(operation, angle):
    angle_rad = math.radians(angle)
    if operation == 'sin':
        return math.sin(angle_rad)
    elif operation == 'cos':
        return math.cos(angle_rad)
    elif operation == 'tan':
        return math.tan(angle_rad)
    else:
        return "Invalid trigonometric function"

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Evaluate Expression")
    print("6. Trigonometry (sin, cos, tan)")
    
    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        expression = input("Enter the expression: ")
        print(f"The result of the expression '{expression}' is {evaluate_expression(expression)}")
    elif choice == '6':
        trig_function = input("Enter the trigonometric function (sin, cos, tan): ")
        angle = float(input("Enter the angle in degrees: "))
        print(f"The result of {trig_function}({angle}) is {trigonometry(trig_function, angle)}")
    else:
        print("Invalid input")

# Run the calculator
calculator()

