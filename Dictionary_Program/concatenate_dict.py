dict1 = {1:1, 2:4}
dict2 = {3:9, 4:16}
dict3 = {5:25, 6:36}

new_dict = {}

for i in (dict1, dict2, dict3):
    new_dict.update(i)

print("New Dictionary = ", new_dict)