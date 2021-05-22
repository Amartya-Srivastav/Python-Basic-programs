list = []
n = int(input("Enter the number of elements in list : "))
for i in range(0, n):
    elements = input("Enter element : ")
    list.append(elements)

print("Original List = ", list)

list[0], list[-1] = list[-1], list[0]

print("List after interchange = ", list)