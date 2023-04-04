word_list = []

while True:
    user_input = input("Give me a word: (If you want to end adding words, type E) ").lower()
    if user_input != "e":
        word_list.append(user_input)
    if user_input == "e":
        break
    
def check_word(word_list):
    longest_word = word_list[0]
    for index, word in enumerate(word_list):
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(check_word(word_list=word_list))