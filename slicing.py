names = ["Anna", "Serhii", "Julia", "Jacob", "Mira"]

# Print second and third name
second_third_names = names[1:3]
print("Second and third names:", second_third_names)

# String Slicing
greeting = "Hello, world!"

# Print only the word "Hello"
hello_word = greeting[0:5]
print("Extracted word:", hello_word)

# Slicing with steps:
print(names[::2])
# Slicing with negative steps:
print(names[::-3])

# Reversing a List
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])

print("Last six characters:", greeting[-6:])

full_name = "Albert Einstein"
# Print last name in uppercase
last_name_upper = full_name[-8:].upper()
print("Last name in uppercase:", last_name_upper)

# Manipulating sequences
"""1: Replacing a slice"""
my_list = [1, 2, 3, 4, 5]
my_list[0:3] = ["a", "b"]
print(my_list)
"""2: Deleting a slice"""
my_list = [1, 2, 3, 4, 5]
del my_list[1:3]
print(my_list)
