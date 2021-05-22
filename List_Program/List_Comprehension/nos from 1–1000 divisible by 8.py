num = [i for i in range(1, 1001)]
X = [j for j in num if j % 8 == 0]

# print("Numbers from 1–1000 that are divisible by 8 = ", X)
print("Numbers from 1–1000 that are divisible by 8 = ", * X, sep="\n")

