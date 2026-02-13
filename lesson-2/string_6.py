user_input = input("Please enter the text:")
word = input("Please enter the word you are seeking:")
if word.lower() in user_input.lower():
    print(f"Found '{word}' regardless of its capitalization!")
else:
    print(f"The word '{word} isn't present in sentence'")

