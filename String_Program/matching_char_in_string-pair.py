count = 0

str1 = input("Enter String 1 = ")
set1 = set(str1)

str2 = input("Enter String 2 = ")
set2 = set(str2)

common_characters = set1 & set2
print("Matching Characters = ", len(common_characters))