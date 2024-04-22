"""Ex. 1: Collecting Numbers from User Input"""

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
# This approach assumes valid input (numbers only)
# If the user enters something else, the program will crash
num1 = int(first_number)
num2 = int(second_number)
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)

"""Ex. 2: Collecting Strings from User Input"""

name = input("Please enter your name: ")
mood = input("How are you doing today, {}? ".format(name))
end_message = "I'm also doing {} today, {}! Thanks for talking to me!".format(
    mood, name
)
print(end_message)
