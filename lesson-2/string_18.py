sentence = input("Please enter the text: ")
start = input("Please enter the word at the beginning: ")
end = input("Please enter the word at the end: ")

if sentence.startswith(start) and sentence.endswith(end):
    print(True)
else:
    print(False)
