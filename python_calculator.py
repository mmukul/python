def print_instructions():
    print("Python Calculator :")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiple")
    print("4. Divide")

def ask_input():
    choice = input("What are we calculating today? (1,2,3 or 4) :")
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    return choice, num1, num2

def addition(num1, num2):
    result = num1 + num2
    print(num1, "+", num2, "=", result)

def subtract(num1, num2):
    result = num1 - num2
    print(num1, "-", num2, "=", result)

def multiplication(num1, num2):
    result = num1 * num2
    print(num1, "*", num2, "=", result)

def division(num1, num2):
    result = num1 / num2
    print(num1, "/", num2, "=", result)


def calculate(choice, num1, num2):
    if choice == '1':
        addition(num1, num2)
    elif choice == '2':
        subtract(num1, num2)
    elif choice == '3':
        multiplication(num1, num2)
    elif choice == '4':
        division(num1, num2)
    else:
        print("Invalid Input")

print_instructions()
choice, num1, num2 = ask_input()
calculate(choice, num1, num2)
