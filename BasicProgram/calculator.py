def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("Select operation")
print("1. Add")
print("2. subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter Your Choice = "))

num1 = int(input("Enter First Number = "))
num2 = int(input("Enter Second Number = "))

if choice == 1:
    print("Addition of", num1, "+", num2, " is = ", num1+num2)
elif choice == 2:
    print("Subtraction of", num1, "-", num2, " is = ", num1 - num2)
elif choice == 3:
    print("Multiplication of", num1, "*", num2, " is = ", num1 * num2)
elif choice == 4:
    print("Division of", num1, "/", num2, " is = ", num1 / num2)
else:
    print("Invalid Input! \n Try Again")