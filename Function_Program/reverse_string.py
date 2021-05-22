def reverse(string):
    rev_str = ''
    ind = len(string)
    for i in range(ind):
        rev_str = rev_str + string[ind - 1]
        ind = ind  - 1
    return rev_str

print(reverse('amartya srivastav'))