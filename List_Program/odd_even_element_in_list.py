list = []
odd_list = []
even_list = []

n = int(input("Enter no of list elements : "))

for i in range(0, n):
    element = int(input("Enter elements : "))
    list.append(element)

for j in range(n):
    if list[j] % 2 == 0:
        even_list.append(list[j])
    else:
        odd_list.append(list[j])

print("Element in odd List is : ", odd_list)
print("Element in even List is : ", even_list)