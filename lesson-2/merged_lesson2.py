
# --- START OF FILE: Boolean_1.py ---
username = input("Please enter your username: ")
password = input("Please enter your password: ")
if bool(username) and bool(password):
    print(True)
else:
    print("Please fill your password or username!")



# --- START OF FILE: Boolean_2.py ---
number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))

print(bool(number1==number2))

# --- START OF FILE: Boolean_3.py ---
number = int(input("Please enter a number: "))
print(bool(number > 0 and number % 2 != 1))

# --- START OF FILE: Boolean_4.py ---
first_number = float(input("Please write the first number:"))
second_number = float(input("Please write the second number:"))
third_number = float(input("Please write the third number:"))

print(bool(first_number != second_number != third_number))


# --- START OF FILE: Boolean_5.py ---
string1 = input("Please enter the first string: ")
string2 = input("Please enter the second string: ")
print(bool(len(string1) == len(string2)))

# --- START OF FILE: Boolean_6.py ---
number = int(input("Please enter a number: "))
print(bool(number % 3 == 0 and number % 5 == 0))


# --- START OF FILE: Boolean_7.py ---
number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))

sum_ = number1 + number2
print(bool(sum_ > 50.8) , bool(10 <= sum_ <= 20))


# --- START OF FILE: Number_Types_1.py ---
number = float(input("Please enter a number:"))
rounded_number = round(number, 2)
print(rounded_number)

# --- START OF FILE: Number_Types_2.py ---
first_number = float(input("Please write the first number:"))
second_number = float(input("Please write the second number:"))
third_number = float(input("Please write the third number:"))

print("The largest number is:" , max(first_number, second_number , third_number))
print("The smallest number is:" , min(first_number, second_number , third_number))

# --- START OF FILE: Number_Types_3.py ---
kilometer = float(input("Please enter length in kilometers:"))
meter = kilometer*1000
centimeter = meter*100
print(kilometer, "-Kilometer")
print(meter, "-meter")
print(centimeter, "-centimeter")

# --- START OF FILE: Number_Types_4.py ---
dividend = int(input("Please enter dividened:"))
divisor = int(input("Please enter dvisor"))
integer_division = dividend // divisor
theremainder = dividend % divisor
print(f"The integer division is {integer_division}\nThe the remainder is {theremainder}")

# --- START OF FILE: Number_Types_5.py ---
celsius = int(input("Please enter celsius:"))
fahrenheit = (celsius * 1.8) + 32
print(f"{celsius} celsius is equal to {fahrenheit} fahrenheit")

# --- START OF FILE: Number_Types_6.py ---
number = int(input("Please enter a number:"))
the_last_digit = int(str(number)[-1])
print(the_last_digit)

# --- START OF FILE: Number_Types_7.py ---
number = int(input("Please enter a number:"))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is not even")

# --- START OF FILE: String_1.py ---
Name = input("What is your name?")
Year = input("What is your year of birth?")
Age = 2026 - int(Year)
print(f"{Name}, you are {Age} years old.")


# --- START OF FILE: String_2.py ---
txt = 'LMaasleitbtui'
car1 = txt[::2]
car2 = txt[1::2]
print(f"{car1} \n \b{car2}") 

# --- START OF FILE: String_3.py ---
string = input("Please enter text:")

print("The length of the text is" , len(string))

print(string.upper())

# --- START OF FILE: String_4.py ---
palindrome = input("Write a word:")
if palindrome == palindrome[::-1]:
    print(f" {palindrome} is palindrome")

# --- START OF FILE: String_5.py ---
txt = input("Please enter a text ")
vowels = 'aeiouAEIOU'

txt_no_spaces = txt.replace(" ", "")

table = str.maketrans('', '', vowels)

number_of_consonants = len(txt_no_spaces.translate(table))

total_letters = len(txt_no_spaces)

number_of_vowels = total_letters - number_of_consonants

print(f"Number of consonants: {number_of_consonants}")
print(f"Number of vowels: {number_of_vowels}")


# --- START OF FILE: string_10.py ---
text = input("Please enter the text: ")
number_of_words = len(text.split())
print(f"The number of words in text are:{number_of_words}")


# --- START OF FILE: string_11.py ---
text = input("Please enter the text: ")
if any(char.isdigit() for char in text):
    print("The text contains digit.")
else:
    print("The text doesn't contain any digit.")

# --- START OF FILE: string_12.py ---
text = input("Please enter the text: ")
print(text.replace(" " , "-"))


# --- START OF FILE: string_13.py ---
print(input("Please enter the text:").replace(" ", ""))


# --- START OF FILE: string_14.py ---
text1 = input("Please enter the first text: ")
text2 = input("Please enter the second text: ")
if text1 == text2:
    print(True)
else:
    print(False)

# --- START OF FILE: string_15.py ---
sentence = input("Please enter the name of organization: ")
words = sentence.split()
acronym = ''
for first_letters in words:
    acronym = acronym + first_letters[0]

print(acronym.upper())

# --- START OF FILE: string_16.py ---
sentence = input("Please enter the text: ")
character = input("Please enter the character you want to delate: ")
replacement = sentence.replace(character, "")
print(replacement)


# --- START OF FILE: string_17.py ---
sentence = input("Please enter the text: ")
vowels = "aeuioAEUIO"
new_text = ""

for char in sentence:
    if char in vowels:
        new_text = new_text + "*"
    else:
        new_text = new_text + char

print(new_text)

# --- START OF FILE: string_18.py ---
sentence = input("Please enter the text: ")
start = input("Please enter the word at the beginning: ")
end = input("Please enter the word at the end: ")

if sentence.startswith(start) and sentence.endswith(end):
    print(True)
else:
    print(False)


# --- START OF FILE: string_6.py ---
user_input = input("Please enter the text:")
word = input("Please enter the word you are seeking:")
if word.lower() in user_input.lower():
    print(f"Found '{word}' regardless of its capitalization!")
else:
    print(f"The word '{word} isn't present in sentence'")



# --- START OF FILE: string_7.py ---
txt = input("Please enter the text:")
word = input("Please enter the word you want to change:")
replacement = input("Please enter the word for replacement:")

Result = txt.replace(word , replacement)
print(Result)


# --- START OF FILE: string_8.py ---
txt = input("Please enter the text:")
print(txt[0] , txt[-1])


# --- START OF FILE: string_9.py ---
txt = input("Please enter the text: ")
print("The reversed text:", txt[::-1])

