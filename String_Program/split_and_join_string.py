string = input("Enter String = ")

new_string = string.split(' ')
print("Splitted String = ", new_string)

string = '-'.join(new_string)
print("Joined String = ", string)

