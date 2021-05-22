arr = [6, 4, 1, 3, 2, 5]
max = arr[0]

for i in range(0, len(arr)):
    if max < arr[i]:
        arr[i] = max

print("Largest element:", max)

# arr = []
# n = int(input("Enter no of elements = "))
# max = arr[0]
#
# for i in range(0, n):
#     if arr[i] > max:
#         max = arr[i]
#     elements = int(input())
#     arr.append(elements)
#
#
# print(arr)
# print("largest", max)
#
