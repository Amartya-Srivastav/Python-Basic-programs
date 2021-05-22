list = ['Apple', 'Banana', 'Chikoo', 'Dragon-Fruit', 'Mango', 'Water Melon']
temp = []

for i in list:
    element = i.split(', ')
    temp.append((element))

Main_List = []

for i in temp:
    element2 = []
    for element in i:
        element2.append(element)
    Main_List.append(element2)

print("Main_List = ", Main_List)