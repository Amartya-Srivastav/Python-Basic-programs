def pascal(n):
    row = [1]
    y = [0]
    for i in range(n):
        print(row)
        row = [l + r for l, r in zip(row + y, y + row)]
    return n>= 1

pascal(6)