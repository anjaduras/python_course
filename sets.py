#1: Ways of defining sets
'''set([1,2,3]) can be used as a difinition but 
there is no built-in way to assign a name for it directly.
The set() function simply returns a new set object based on the 
provided iterable (like a list or another set).'''

set1 = {1,2,3}
l = [3,4,5]
set2 = set(l)
print(set1,set2)
print(f"The length of the first set equals {len(set1)}")