def check_case(character):
    if character.isalpha() and len(character) == 1:
        if character.isupper():
            return "The character is uppercase."
        elif character.islower():
            return "The character is lowercase."
    else:
        return "Please enter a single alphabet character."
char = input("Enter a character: ")
result = check_case(char)
print(result)
