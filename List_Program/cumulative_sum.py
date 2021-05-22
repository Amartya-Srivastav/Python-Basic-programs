list = []
list1 = []
j = 0
n = int(input("Enter no of elements : "))

for i in range(0, n):
    elements = int(input("Enter elements = "))
    list.append(elements)
    j = j + list[i]
    list1.append(j)

print("original List = ", list)
print("Cumulative sum list = ", list1)