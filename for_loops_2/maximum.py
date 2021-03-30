def maximum(list):
    if len(list) == 0:
        return False
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

print(maximum([37, 2, 1, -9]))
print(maximum([]))
