## MAking a simple calculator in Python
def run():
    print("Choose one operarion from the following list:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

# Take input from the user
    operation =input("Enter operation (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if operation == '1':
        print(num1, "+", num2, "=", num1 + num2)
    elif operation == '2':
        print(num1, "-", num2, "=", num1 - num2)
    elif operation == '3':
            print(num1, "*", num2, "=", num1 * num2)
    elif operation == '4':
        if num2 != 0:
         print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid input")  