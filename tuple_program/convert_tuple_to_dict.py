lst = []
n = int(input("Enter no of elements = "))

for i in range(0, n):
    ele = int(input())
    lst.append(ele)

print("Original list = ", (tuple(lst)))

dict = tuple(lst)
print(dict)