string = input("Enter a string = ")
add = input("Enter the string to add = ")

index = int(input("Enter indexing = "))

for i in string:
    new_string = string[:index] + add + string[index:]

print("String after performing addition = ", new_string)





