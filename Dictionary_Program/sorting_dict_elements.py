dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original Dictionary = ", dictionary)

new_dict = dict(sorted(dictionary.items()))

print("Sorted Dictionary = ", new_dict)