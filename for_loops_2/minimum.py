def minimum(list):
    if len(list) == 0:
        return False
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

print(minimum([37, 2, 1, -9]))
print(minimum([]))