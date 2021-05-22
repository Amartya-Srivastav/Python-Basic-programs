string = input("Enter string = ")
new_string = " "
for i in range(len(string)):
    if i % 2 != 0:
        new_string = new_string + string[i]

print("Displaying only even index characters of the string = ", new_string)

