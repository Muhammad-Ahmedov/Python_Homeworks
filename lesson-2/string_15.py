sentence = input("Please enter the name of organization: ")
words = sentence.split()
acronym = ''
for first_letters in words:
    acronym = acronym + first_letters[0]

print(acronym.upper())