num1 = int(input("Enter First Number = "))
fact = 1

if num1 == 0:
    print("Enter Positive value")
elif num1 == 1:
    print("Factorial of 1 is 0")
else:
    for i in range(1, num1+1):
        fact = fact * i
    print("The Factorial of", num1, "is", fact)
