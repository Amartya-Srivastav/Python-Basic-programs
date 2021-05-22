def multiply(list):
    count = 1
    for i in list:
        count = count * i
    return count

print(multiply((1, 2, 3, 4, 5)))