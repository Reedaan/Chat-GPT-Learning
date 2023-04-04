user_input = input("Provide numbers you want to sum: ")
user_input_data = []
sum = 0

for index, a in enumerate(user_input):
    user_input_data.append(a)
    
for number in user_input_data:
    sum = sum + int(number)
    
print(sum)