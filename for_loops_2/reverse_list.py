def reverse_list(list):
    half_len = int(len(list) / 2)
    for i in range(half_len):
        list[i] , list[len(list) - 1 - i] = list[len(list) - 1 - i], list[i]
    return list

print(reverse_list([37, 2, 1, -9]))
print(reverse_list([37, 2, 1, -9, 5]))
print(reverse_list([]))
print(reverse_list([1]))
print(reverse_list([1, 2]))