X = [[1, 2],
     [3, 4],
     [5, 6]]
for row in X:
    print(row)

Y = [[X[i][j] for i in range(len(X))] for j in range(len(X[0]))]
print("\n")

for row in Y:
    print(row)