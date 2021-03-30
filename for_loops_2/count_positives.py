def count_positives(list):
    count = 0
    for i in list:
        if i > 0:
            count += 1
    list[len(list) - 1] = count
    return list

print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))