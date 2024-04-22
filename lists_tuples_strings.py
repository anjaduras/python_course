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

"""Common string Methods"""
print("Hello World!".lower())
print("Hello World!".upper())
print("one two three".title())

s1 = "süß"
print(s1.casefold)

print("    This string was stripped!".lstrip())
print("And I'm back home".rstrip("home"))

print(",".join(["10", "20", "30"]))
data = "10,20,30"
print(data.split(","))
print(data.index("20"))
print(data.endswith("30"))

# Manipulating sequences
"""To append multiple elements we can extend the sequence:"""
my_list = [1, 2, 3]
my_list.extend("abc")
print(my_list)

"""We can also insert element into the sequence. Its not recommended to use often as it is much slower then appending or extending and it also shifts 
all the other elements to the RHS"""
my_list = [2, 3, 4, 5]
my_list.insert(0, 100)
print(my_list)
my_list.insert(4, 4.5)
print(my_list)

# Unpacking a sequence
gagaboni = ("Anja", 18, "boba tea")
(name, age, drink) = gagaboni
print(name)
print(age)
print(drink)
