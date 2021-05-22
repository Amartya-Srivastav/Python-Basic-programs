X = [[6, 4, 2],
     [8, 7, 9],
     [1, 3, 5]]

Y = [[2, 5, 6],
     [6, 5, 4],
     [7, 3, 1]]


Total = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        Total[i][j] = X[i][j] * Y[i][j]

print("Addition of Two Matrices = ")

for k in Total:
    print(k)