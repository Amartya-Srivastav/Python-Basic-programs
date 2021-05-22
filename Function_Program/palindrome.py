def palindrome(string):
    return string == string[::-1]

string = input("Enter String = ")
ans = palindrome(string)
if ans:
    print("Yes")
else:
    print("No")
    
