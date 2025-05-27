def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


a = int(input("Enter a: "))
b = int(input("Enter b: "))

even_numbers = list(range(a if a % 2 == 0 else a + 1, b + 1, 2)) if a <= b else []
print(even_numbers)


a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Adjust start to the next even number if a is odd
start = a + a % 2
even_numbers = list(range(start, b + 1, 2))
print(even_numbers)
