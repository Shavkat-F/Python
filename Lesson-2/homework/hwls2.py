from datetime import datetime

name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
current_year = datetime.now().year
age = current_year - birth_year

print(f"{name}, you are {age} years old.")


txt = 'LMaasleitbtui'
car_name = txt[::2]  # Skipping every second character
print("Car name:", car_name)


txt = 'MsaatmiazD'
car_name = txt[::2]
print("Car name:", car_name)


txt = "I'am John. I am from London"
area = txt.split("from")[-1].strip()
print("Residence area:", area)


text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)


text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
max_value = max(numbers)
print("Maximum value:", max_value)



word = input("Enter a word: ")
if word == word[::-1]:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")


email = input("Enter your email address: ")
domain = email.split('@')[-1]
print("Domain:", domain)


import random
import string

length = 12  # You can change the length
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))

print("Random password:", password)
