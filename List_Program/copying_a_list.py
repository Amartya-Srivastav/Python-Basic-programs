list = []
n = int(input("Enter no of elements : "))

for i in range(0, n):
    elements = int(input("Enter elements = "))
    list.append(elements)
print("original List = ", list)

list1 = list.copy()

print("New Copied List = ", list1)