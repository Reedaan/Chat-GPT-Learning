input_list = [5, 10, 8, 15, 20, 25]

def second_largest(list):
    list = sorted(list)
    return list[-2]

second_largest(list=input_list)