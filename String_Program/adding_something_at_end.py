# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged

string = input("Enter String = ")
length = len(string)

if length > 2:
    if string[-3:] == "ing":
        string = string + "ly"
    else:
        string = string + "ing"

print(string)

