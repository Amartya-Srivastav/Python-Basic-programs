list = []
n = int(input("Enter Elements = "))
for i in range(0, n):
    element = input()
    list.append(element)

print("Original List = ", list)

# Several methods to reverse a list

# 1. list.reverse()
# 2. rev_list = list[::-1]

print("Reversed List = ", list)