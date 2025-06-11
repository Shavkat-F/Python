python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
pip install numpy

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

# Can be left empty or use to import functions directly
from .circle import calculate_area, calculate_circumference

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

from .file_reader import read_file
from .file_writer import write_file

