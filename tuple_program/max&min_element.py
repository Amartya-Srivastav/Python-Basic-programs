list = []
n = int(input("Enter no of element = "))

for i in range(0, n):
    ele = input("Enter element = ")
    list.append(ele)

ma = max(list)
mi = min(list)

for j in range(len(list)):
    if list[i] >= ma:
        ma = list[i]
    elif list[i] <= mi:
        mi = list[i]

t = tuple(list)

print("Tuple = ", t)
print("Max element = ", ma)
print("Minimum element = ", mi)

