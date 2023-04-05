data_string = "Hello there! How are you doing today? Are you enjoying learning Python?".lower()

def check_unique(string):
    words = string.split(" ")
    words = list(dict.fromkeys(words))
    return sorted(words)
    
print(check_unique(string=data_string))