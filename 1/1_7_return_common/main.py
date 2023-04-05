a = [1, 2, 3, 6, 7, 8, 9, 11, 15, 16, 18, 22, 65]
b = [1, 2, 3, 6, 11, 15, 16, 65, 100, 123, 95]

set_b = set(b)

def is_common(a, set_b):
    
    common = []
    for number in a:
        if number in set_b:
            common.append(number)
    return common

print(is_common(a, set_b))