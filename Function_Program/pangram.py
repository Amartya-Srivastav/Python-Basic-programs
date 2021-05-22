import string


def pangram(str, a = string.ascii_lowercase):
    a = set(a)
    return a<= set(str.lower())

print(pangram('The quick brown fox jumps over lazy dog'))