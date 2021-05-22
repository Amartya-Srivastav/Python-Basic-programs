str = input("Enter a string = ")
dict = {}

for i in str:
    keys = dict.keys()
    if i in keys:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1

print("Each Character Frequency = ", dict)
