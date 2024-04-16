# Exercise 1
class Sportcar:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


modelX = Sportcar(250, 30)
print(modelX.max_speed, modelX.mileage)


# Exercise 2
class Dog:
    def __init__(
        self,
        name,
        breed,
        age,
    ):
        self.name = name
        self.breed = breed
        self.age = age


Dog1 = Dog("Bobby", "Beagle", 3)
print(
    f"This dog is named {Dog1.name}. It's a {Dog1.breed} that is {Dog1.age} years old."
)


# Exercise 3
class Student:
    def __init__(self, name, age, dream):
        self.name = name
        self.age = age
        self.dream = dream


Student1 = Student("Lucy", 21, "work at the police station")
Student2 = Student("Stacy", 26, "become a pilot")
Student3 = Student("Adrian", 23, "get a cat")
print(
    f"Welcome to the class.\n First student is {Student1.name}, she's {Student1.age} years old and her dream is to {Student1.dream}. \n Second student is {Student2.name}, she's {Student2.age} years old and her dream is to {Student2.dream}. \n Third student is {Student3.name}, he's {Student3.age} years old and his dream is to {Student3.dream}."
)
