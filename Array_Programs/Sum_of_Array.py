arr = []
n = int(input("Enter number of elements = "))

for i in range(0, n):
    elements = int(input())
    arr.append(elements)

print(arr)

Sum = sum(arr)
print("Sum of array = ", Sum)