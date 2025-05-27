my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}

# Ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", sorted_dict_asc)

# Descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", sorted_dict_desc)

my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Merging dictionaries
result = {**dic1, **dic2, **dic3}
print(result)

n = 5
squares = {x: x*x for x in range(1, n+1)}
print(squares)

squares = {x: x*x for x in range(1, 16)}
print(squares)

my_set = set([1, 2, 3])
print(my_set)

my_set = {1, 2, 3, 4}
for item in my_set:
    print(item)

my_set = {1, 2}
my_set.add(3)
my_set.update([4, 5])
print(my_set)

my_set = {1, 2, 3, 4}
my_set.remove(3)  # Will raise KeyError if item is not found
print(my_set)

my_set = {1, 2, 3}
my_set.discard(2)  # No error if item is not found
print(my_set)

