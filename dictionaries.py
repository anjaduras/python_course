'''Program about family roles, that's why they are keys. 
if it was about our exact family, our names would be keys'''

family = {
    "Mom" : "Julia",
    "Dad" : "Serhii",
    "Daughter" : "Anna",
    "Son" : "Jacob"
}

family["Daughter"] = "Anja"
print(family)
family["Pet"] = "Mira"
print(family)
for name, role in family.items():
    print(f"{role}: {name}")