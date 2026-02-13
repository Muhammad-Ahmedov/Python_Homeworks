text = input("Please enter the text: ")
if any(char.isdigit() for char in text):
    print("The text contains digit.")
else:
    print("The text doesn't contain any digit.")