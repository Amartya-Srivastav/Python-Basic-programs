list = []
n = int(input("Enter no of elements : "))

for i in range(0, n):
    elements = int(input("Enter elements = "))
    list.append(elements)
print("original List = ", list)

list1 = set(list)

print("Final list = ", sorted(list1))