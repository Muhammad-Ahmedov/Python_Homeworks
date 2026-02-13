txt = input("Please enter a text ")
vowels = 'aeiouAEIOU'

txt_no_spaces = txt.replace(" ", "")

table = str.maketrans('', '', vowels)

number_of_consonants = len(txt_no_spaces.translate(table))

total_letters = len(txt_no_spaces)

number_of_vowels = total_letters - number_of_consonants

print(f"Number of consonants: {number_of_consonants}")
print(f"Number of vowels: {number_of_vowels}")
