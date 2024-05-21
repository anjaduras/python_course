# 1: Ways of defining sets

"""set([1,2,3]) can be used as a difinition but 
there is no built-in way to assign a name for it directly.
The set() function simply returns a new set object based on the 
provided iterable (like a list or another set)."""

set1 = {1, 2, 3}
l = [3, 4, 5]
set2 = set(l)
print(set1, set2)
print(f"The length of the first set equals {len(set1)}")
print()

# 2: Disjointedness
print(set1.isdisjoint(set2))
# Prints False because these two sets have a joined element.
print()

# 3: Add, Remove and Discard
set1.add(4)
set1.add(1)
print(set1)
set1.remove(4)
# set1.remove(100) returns a KeyError. However
set1.discard(100)
print(set1)
print()

# 4: Union VS Intersection
print(set1 | set2)
print(set1 & set2)
print()

# 5: Difference
print(set1 - set2)
print(set2 - set1)
# SHowcase of set difference being uncommutative.
print(set1 - set1)
print()

#6:Set Comprehensions
numbers = {x for x in range(1, 11) if x % 2 == 0}  
print(numbers)
print()

#7: Findind Unique Characters
text = "hello world"
unique_chars = set(text)
print(unique_chars)
#May not follow the exact order of elements