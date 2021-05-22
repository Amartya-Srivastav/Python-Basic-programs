X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print("Original Matrix = ", X)

Y = 2

Z = [a[Y] for a in X]

print("The Kth column of matrix is : " + str(Z))