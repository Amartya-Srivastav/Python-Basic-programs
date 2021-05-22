p = int(input("Enter Principle amt = "))
r = int(input("Enter rate = "))
t = int(input("Enter time = "))

for i in range(t):
    p = p + ((p*r)/100)
print("Compound Interest = ", p)
