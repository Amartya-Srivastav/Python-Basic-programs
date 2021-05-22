def sum(a, b):
    if a > b:
        return a
    return b

def sum2(a, b, c):
    return sum(a, sum(b, c))

print(sum2(3, 1, 6))

