list = []
n = int(input("Enter the number of elements in list : "))
for i in range(0, n):
    elements = input("Enter element : ")
    list.append(elements)

print("Enter indexes to be swapped = ")
i1 = int(input("Index 1 = "))
i2 = int(input("Index 2 = "))

print("Initial List = ", list)

list[i1], list[i2] = list[i2], list[i1]

print("List after swapping = ", list)