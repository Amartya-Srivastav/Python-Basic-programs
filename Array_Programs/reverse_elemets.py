arr = []
n = int(input("Enter no of elements = "))

for i in range(0, n):
    elements = int(input())
    arr.append(elements)

print("Original Array = ", arr)
arr.reverse()
print("Reversed Array = ", arr)