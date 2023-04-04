a = [1, 2, 3, 6, 7, 8, 9, 11, 15, 16, 18, 22, 65]
b = [1, 2, 3, 6, 11, 15, 16, 65, 100, 123, 95]



def is_common(a, b):
    for index, number in enumerate(a):
        if a[index] in b:
            print(number)
    
print(is_common(a, b))