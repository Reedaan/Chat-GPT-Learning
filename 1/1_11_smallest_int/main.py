data = [1, 2, 3, 4, 5, 6]

def is_smallest(data):
    smallest_number = data[0]
    for number in data:
        if number < smallest_number:
            smallest_number = number
    return smallest_number

print(is_smallest(data))