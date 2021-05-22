list = []
n = int(input("Enter no of element = "))

for i in range(0, n):
    ele = input("Enter element = ")
    list.append(ele)

t = tuple(list)
print(t)