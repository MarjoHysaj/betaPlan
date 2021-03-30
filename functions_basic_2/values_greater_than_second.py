def greater_than_second(list):
    new_list = []
    second_value = list[1]
    for i in range(len(list)):
        if list[i] > second_value:
            new_list.append(list[i])
        print(len(new_list))
        return new_list
print(greater_than_second([5,2,3,2,1,4]))
