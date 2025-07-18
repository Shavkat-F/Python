import numpy as np

# Task 1: Convert list to 1‑D array
lst = [12.23, 13.32, 100, 36.32]
arr1 = np.array(lst)
print("Task 1:")
print("Original List:", lst)
print("One‑dimensional NumPy array:", arr1, "\n")

# Task 2: 3×3 matrix with values 2→10
matrix = np.arange(2, 11).reshape(3, 3)
print("Task 2:")
print(matrix, "\n")

# Task 3: Null vector of size 10 & update 7‑th (index 6) value to 11
null_vec = np.zeros(10)
print("Task 3:")
print("Null vector:", null_vec)
null_vec[6] = 11          # 7‑th element (matches the example output)
print("After update:", null_vec, "\n")

# Task 4: Array with values 12→37
arr2 = np.arange(12, 38)
print("Task 4:")
print(arr2, "\n")

# Task 5: Convert array to float
arr3 = np.array([1, 2, 3, 4])
arr3_float = arr3.astype(float)
print("Task 5:")
print("Original array:", arr3)
print("Converted to float type:", arr3_float, "\n")

# Task 6: Celsius → Fahrenheit conversion
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = celsius * 9/5 + 32
print("Task 6:")
print("Values in Celsius degrees:", np.round(celsius, 2))
print("Values in Fahrenheit degrees:", np.round(fahrenheit, 2), "\n")

# (Optional) convert back to verify
c_back = (fahrenheit - 32) * 5/9
print("Back‑converted to Celsius (check):", np.round(c_back, 2), "\n")

# Task 7: Append values to array
orig_arr = np.array([10, 20, 30])
appended = np.append(orig_arr, [40, 50, 60, 70, 80, 90])
print("Task 7:")
print("Original array:", orig_arr)
print("After appending:", appended, "\n")

# Task 8: Statistics on random array of 10 elements
np.random.seed(0)
rand_arr = np.random.rand(10)
print("Task 8:")
print("Random array:", rand_arr)
print("Mean:", rand_arr.mean())
print("Median:", np.median(rand_arr))
print("Standard deviation:", rand_arr.std(), "\n")

# Task 9: 10×10 random array – min & max
rand_10x10 = np.random.rand(10, 10)
print("Task 9:")
print("10×10 random array:\n", rand_10x10)
print("Minimum value:", rand_10x10.min())
print("Maximum value:", rand_10x10.max(), "\n")

# Task 10: 3×3×3 random array
rand_3x3x3 = np.random.rand(3, 3, 3)
print("Task 10:")
print("3×3×3 random array:\n", rand_3x3x3)
