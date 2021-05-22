list = []
n = int(input("Enter Elements = "))
for i in range(0, n):
    element = input()
    list.append(element)

print("Original List = ", list)

# Several ways to delete / clear list

# 1. list *= 0
# 2. list.clear()
# 3. del list[:]

print("Deleted list = ", list)

