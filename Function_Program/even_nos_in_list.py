def even(list):
    even_list = []
    for i in range(len(list)):
        if i % 2 == 0:
            even_list.append(i)
    return even_list

print(even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))