year = int(input("Enter Year = "))
if year % 400 == 0:
    print(year, "Is a leap year")
elif year % 100 == 0:
    print(year, "Is not a leap year")
elif year % 4 == 0:
    print(year, "Is a leap year")
else:
    print(year, "Is not a leap year")
print(year) 