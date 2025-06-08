# Exception Handling Exercises

# 1. Handle ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 2. Raise ValueError for invalid integer input
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("That's not a valid integer.")

# 3. Handle FileNotFoundError
try:
    with open('nonexistent.txt') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")

# 4. Raise TypeError for non-numeric input
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    raise TypeError("Inputs must be numbers.")

# 5. Handle PermissionError
try:
    with open('/root/secret.txt') as f:
        print(f.read())
except PermissionError:
    print("You do not have permission to access this file.")

# 6. Handle IndexError in list operation
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range.")

# 7. Handle KeyboardInterrupt
try:
    input("Press Ctrl+C to interrupt: ")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")

# 8. Handle ArithmeticError
try:
    result = 10 ** 10000
except ArithmeticError:
    print("Arithmetic error occurred.")

# 9. Handle UnicodeDecodeError
try:
    with open('unicode.txt', encoding='ascii') as f:
        print(f.read())
except UnicodeDecodeError:
    print("Encoding issue reading file.")

# 10. Handle AttributeError
try:
    x = [1, 2, 3]
    x.appendd(4)
except AttributeError:
    print("Attribute does not exist.")

# File Input/Output Exercises

# 11. Read entire file
with open('example.txt', 'r') as f:
    print(f.read())

# 12. Read first n lines
n = 3
with open('example.txt') as f:
    for i in range(n):
        print(f.readline().strip())

# 13. Append and display text
with open('example.txt', 'a+') as f:
    f.write('\nAppended line.')
    f.seek(0)
    print(f.read())

# 14. Read last n lines
with open('example.txt') as f:
    lines = f.readlines()
    print(''.join(lines[-3:]))

# 15. Read lines into list
with open('example.txt') as f:
    lines_list = f.readlines()

# 16. Read lines into variable
with open('example.txt') as f:
    content = f.read()

# 17. Read lines into array
with open('example.txt') as f:
    array = [line.strip() for line in f]

# 18. Find longest words
with open('example.txt') as f:
    words = f.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)

# 19. Count lines
with open('example.txt') as f:
    print("Number of lines:", sum(1 for _ in f))

# 20. Word frequency
from collections import Counter
with open('example.txt') as f:
    freq = Counter(f.read().replace(',', ' ').split())
    print(freq)

# 21. File size
import os
print("Size:", os.path.getsize('example.txt'), "bytes")

# 22. Write list to file
data = ['apple', 'banana', 'cherry']
with open('list.txt', 'w') as f:
    f.write('\n'.join(data))

# 23. Copy file contents
with open('example.txt') as f1, open('copy.txt', 'w') as f2:
    f2.write(f1.read())

# 24. Combine lines from 2 files
with open('file1.txt') as f1, open('file2.txt') as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " " + l2.strip())

# 25. Read random line
import random
with open('example.txt') as f:
    lines = f.readlines()
    print(random.choice(lines))

# 26. Check if file is closed
f = open('example.txt')
print("Closed?", f.closed)
f.close()

# 27. Remove newlines
with open('example.txt') as f:
    print(''.join(f.read().splitlines()))

# 28. Count words in file
with open('example.txt') as f:
    print("Word count:", len(f.read().replace(',', ' ').split()))

# 29. Extract characters from multiple files
chars = []
for fname in ['a.txt', 'b.txt']:
    with open(fname) as f:
        chars.extend(list(f.read()))
print(chars)

# 30. Generate A.txt to Z.txt
import string
for letter in string.ascii_uppercase:
    with open(f'{letter}.txt', 'w') as f:
        f.write(f"This is file {letter}\n")

# 31. Alphabet file with letters per line
import textwrap
with open('alphabet.txt', 'w') as f:
    f.write('\n'.join(textwrap.wrap(string.ascii_lowercase, 4)))
