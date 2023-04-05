data_list = [3, 2, 4, 5, 8, 9]

def sum_list(list):
    
    sum = 0
    for a in list:
        if a % 2 == 0:
            sum = sum + a
    return sum
        
print(sum_list(data_list))