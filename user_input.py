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

"""Ex 3: Simplest Compatability Test"""

number = 0
print("Welcome to my first Python Quizz! Let's check if we are compatible:)")
user_q1 = input(
    "Do you listen to music (yes/no)? "
).lower()  # Get user choice in lowercase
user_q2 = input("Do you like cats (yes/no)? ").lower()
user_q3 = input("Do you drink coffee (yes/no)? ").lower()
user_q4 = input("Do you have long-term goals of any kind (yes/no)? ").lower()

number += 5 if user_q1 == "yes" else 0
number += 5 if user_q2 == "yes" else 0
number += 5 if user_q3 == "yes" else 0
number += 5 if user_q4 == "yes" else 0

if number <= 5:
    print("Your score on my quiz is {}. We can't be friends :((".format(number))
elif 10 <= number <= 15:
    print("Your score on my quiz is {}. You're cool! Let's hang out.".format(number))
elif number == 20:
    print(
        "Your score on my quiz is {}! Omg, are we soulmates? Because I sure think so!".format(
            number
        )
    )
else:
    print(
        "Your score is",
        number,
        ". This result is unexpected. Please check the quiz logic.",
    )
