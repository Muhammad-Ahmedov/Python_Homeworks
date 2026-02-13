sentence = input("Please enter the text: ")
vowels = "aeuioAEUIO"
new_text = ""

for char in sentence:
    if char in vowels:
        new_text = new_text + "*"
    else:
        new_text = new_text + char

print(new_text)