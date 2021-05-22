list = []
n = int(input("Enter no of elements : "))

for i in range(0, n):
    element = int(input("Enter elements : "))
    list.append(element)

print("Original List", list)

print("Smallest Element = ", min(list))