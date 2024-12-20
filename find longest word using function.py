word_list=["banana", "cherry", "apple", "orange", "pineapple"]
max_length=0
def longest_word (word):
    longest=""
    max_length= 0
    for word in word_list:
        if len(word)> max_length:
            longest = word
            max_length = len(word)
    return longest
result=longest_word(word_list)
print(f"the longest word is {result} and its length is {len(result)}")