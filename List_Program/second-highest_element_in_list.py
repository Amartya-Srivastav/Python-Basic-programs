list = []
n = int(input("Enter no of elements : "))

for i in range(0, n):
    element = int(input("Enter elements : "))
    list.append(element)

print("Original List", list)
print("Sorted list = ", sorted(list))
print("Second Highest Element = ", sorted(list)[-2])