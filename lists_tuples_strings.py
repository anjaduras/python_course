# Lists
cats = ["Ragdoll", "Main coon", "Persian", "Abyssinian", "Sphynx"]

# Basic
print(cats[1])
print(cats[0])
cats.append("Siamese")
print(cats)

# Add numbers
for i, cat in enumerate(cats):
    print(f"{i+1}. {cat}")

# Reverse the list
for cat in reversed(cats):
    print(cat)

# Remove the first element
first_cat = cats.pop(0)
print(f"Removed first cat: {first_cat}")
print(cats)

# Sort the list alphabetically
cats.sort()
print(cats)

# Numbers from 1 to 10
numbers = [x for x in range(1, 11)]
print(numbers)

# Squares of numbers in the list
squares = [x * x for x in numbers]
print(squares)

# Tuples
"""(Tuples) are like lists but immutable and faster (hold less memory). So I'm not doing extra exercizes on them."""

# Strings
"""Those are also self explainatory, not doing extra exercizes"""
