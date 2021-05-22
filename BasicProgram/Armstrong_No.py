num = int(input("Enter Number = "))
count=0
sum = 0

temp = num

while temp > 0:
    digit = temp % 10
    count=count+1
    temp //= 10
a=num
while a > 0:
    digit = a % 10
    a //= 10
    sum = sum + (digit ** count)

if num == sum:
  print(num,"is an Armstrong number")
else:
  print(num,"is not an Armstrong number")