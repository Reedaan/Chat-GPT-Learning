data = int(input("Provide numbers to check which ones are prime numbers: "))

b = 0
for a in range(1, data):
    if data % a == 0:
        b += 1
        
if b == 1:
    is_Prime = True
else:
    is_Prime = False
        
if is_Prime:
    print("It's a prime number")
else:
    print("It's not a prime number")
