# 1. Modify String with Underscores
def insert_underscores(txt):
    result = ""
    i = 0
    count = 0
    vowels = "aeiouAEIOU"
    while i < len(txt):
        result += txt[i]
        count += 1
        if count == 3:
            if i + 1 < len(txt) and (txt[i + 1] in vowels or txt[i + 1] == '_'):
                count = 0
                i += 1
                result += txt[i]
            if i + 1 < len(txt):
                result += "_"
            count = 0
        i += 1
    if result.endswith('_'):
        result = result[:-1]
    return result

print("1. Modify String with Underscores:")
print(insert_underscores("hello"))
print(insert_underscores("assalom"))
print(insert_underscores("abcabcabcdeabcdefabcdefg"))
print()

# 2. Integer Squares
print("2. Integer Squares:")
n = 5
for i in range(n):
    print(i ** 2)
print()

# 3. Loop-Based Exercises

print("3.1. First 10 Natural Numbers:")
i = 1
while i <= 10:
    print(i)
    i += 1
print()

print("3.2. Pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
print()

print("3.3. Sum from 1 to n:")
n = 10
total = sum(range(1, n + 1))
print("Sum is:", total)
print()

print("3.4. Multiplication Table:")
num = 2
for i in range(1, 11):
    print(num * i)
print()

print("3.5. Display Numbers from List (75 to 150):")
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 150 >= num >= 75:
        print(num)
print()

print("3.6. Count Digits in Number:")
num = 75869
count = 0
while num > 0:
    num //= 10
    count += 1
print("Output:", count)
print()

print("3.7. Reverse Number Pattern:")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
print()

print("3.8. List in Reverse Order:")
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)
print()

print("3.9. Numbers from -10 to -1:")
for i in range(-10, 0):
    print(i)
print()

print("3.10. Done After Loop:")
for i in range(5):
    print(i)
else:
    print("Done!")
print()

print("3.11. Prime Numbers Between 25 and 50:")
start = 25
end = 50
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
print()

print("3.12. Fibonacci Series up to 10 Terms:")
a, b = 0, 1
for _ in range(10):
    print(a, end='  ')
    a, b = b, a + b
print("\n")

print("3.13. Factorial of Number:")
n = 5
fact = 1
for i in range(2, n + 1):
    fact *= i
print(f"{n}! = {fact}")
print()

# 4. Return Uncommon Elements of Lists
from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []
    for k in (c1.keys() | c2.keys()):
        if c1[k] != c2[k]:
            result.extend([k] * abs(c1[k] - c2[k]))
    return result

print("4. Uncommon Elements Between Lists:")
print(uncommon_elements([1, 1, 2], [2, 3, 4]))
print(uncommon_elements([1, 2, 3], [4, 5, 6]))
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))
