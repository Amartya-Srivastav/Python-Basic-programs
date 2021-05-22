num = [i for i in range(1, 1001)]
X = [j for j in num if "6" in str(j)]

print("Numbers from 1–1000 that have a 6 in them = ", *X, sep="\n")

