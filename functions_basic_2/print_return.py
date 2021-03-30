my_list = [2,3]
def print_return():
    for i in range(len(my_list)):
        print(my_list[0])
        return my_list[1]
print_return()
