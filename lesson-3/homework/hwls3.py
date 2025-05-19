fruits = ['apple', 'banana', 'cherry', 'orange', 'grape']
print("Third fruit:", fruits[2])

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
print("Concatenated list:", concatenated)

numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print("Extracted elements:", new_list)

movies = ['Inception', 'Interstellar', 'Matrix', 'Gladiator', 'Coco']
movies_tuple = tuple(movies)
print("Movies tuple:", movies_tuple)

cities = ['New York', 'London', 'Paris', 'Tokyo']
is_paris_present = "Paris" in cities
print("Is Paris in the list?", is_paris_present)

original_list = [1, 2, 3]
duplicated_list = original_list * 2
print("Duplicated list:", duplicated_list)

numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("Swapped list:", numbers)

num_tuple = tuple(range(1, 11))
sliced = num_tuple[3:8]
print("Sliced tuple (index 3 to 7):", sliced)

colors = ['red', 'blue', 'green', 'blue', 'yellow', 'blue']
blue_count = colors.count('blue')
print("Number of times 'blue' appears:", blue_count)

animals = ('cat', 'dog', 'lion', 'tiger', 'elephant')
lion_index = animals.index('lion')
print("Index of 'lion':", lion_index)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print("Merged tuple:", merged_tuple)

sample_list = [1, 2, 3, 4, 5]
sample_tuple = (10, 20, 30)
print("Length of list:", len(sample_list))
print("Length of tuple:", len(sample_tuple))

number_tuple = (11, 22, 33, 44, 55)
converted_list = list(number_tuple)
print("Converted list:", converted_list)

number_tuple = (3, 7, 2, 9, 5)
print("Maximum:", max(number_tuple))
print("Minimum:", min(number_tuple))

words = ('hello', 'world', 'python', 'rocks')
reversed_tuple = words[::-1]
print("Reversed tuple:", reversed_tuple)
