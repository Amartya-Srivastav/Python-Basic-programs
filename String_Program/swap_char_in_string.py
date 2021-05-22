string = input("Enter String = ")
for i in string:
    string = string[-1:] + string[1:-1] + string[:1]

print("Swapped Sring = ",string)