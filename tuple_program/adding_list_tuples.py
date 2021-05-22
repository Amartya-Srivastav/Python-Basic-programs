# lst = [1, 2, 3, 4]
# lst.extend([5, 6, 7, 8])
#
# print(tuple(lst))

lst = []
n = int(input("Enter no of elements = "))

for i in range(0, n):
    ele = int(input())
    lst.append(ele)

print("Original list = ", lst)

lst.extend([int(input("Enter next element = "))])

print("Updated list = ", tuple(lst))
