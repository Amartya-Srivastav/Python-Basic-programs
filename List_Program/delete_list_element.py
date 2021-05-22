list = []
n = int(input("Enter no of elements : "))

for i in range(0, n):
    elements = int(input("Enter elements = "))
    list.append(elements)
print("original List = ", list)

del list[:]
print("Deleted list = ", list)