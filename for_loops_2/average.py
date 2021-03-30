def average(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)
print(average([1 ,2 ,3 , 4]))
