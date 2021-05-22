n = int(input("Enter the number of terms: "))
n1 = 0
n2 = 1
count = 2

if n <= 0:
    print("Enter positive integer")
elif n == 1:
    print("The fibonacci sequence = ", n1)
else:
    print("Fibonacci Sequence :")
    print(n1,",",n2, end =', ')
    while count < n:
        nth=n1+n2
        print(nth,end=', ')
        n1=n2
        n2=nth
        count=count+1