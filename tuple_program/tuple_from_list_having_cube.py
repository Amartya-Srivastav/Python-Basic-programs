# list_cube = []
# n = int(input("Enter no of element = "))
#
# for i in range(0, n):
#     list = (input())
#     for i in list:
#         cube = list[i] ** 3
#         list_cube.append([list, cube])
#
# print(list_cube)

list_cube = []
n = int(input("Enter no of element = "))
l = []
for i in range(0, n):
    list = int(input())
    l.append(list)
for i in l:
    list_cube.append((i, i ** 3))

print(list_cube)

# list = []
# cube = []
#
# n = int(input("Enter no of elements = "))
# for i in range(1, n):
#     list.append(i)
#
# for i in list:
#     cube.append((i, i**3))

