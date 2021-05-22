Lists1 = ["Banana", 3, "Apple", 8, "Mango", 10, "Pineapple", 18, "Grapes", 33]
print("Original list =",Lists1)

Key_List1 = ["NAME", "NUMBER"]
n = len(Lists1)

dict_list = []

for i in range(0, n, 2):
    dict_list.append({Key_List1[0]: Lists1[i], Key_List1[1]: Lists1[i + 1]})

print("\nThe constructed Dictionary-List : " + str(dict_list))

