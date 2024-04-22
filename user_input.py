first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

# This approach assumes valid input (numbers only)
# If the user enters something else, the program will crash
num1 = int(first_number)
num2 = int(second_number)

sum = num1 + num2

print("The sum of", num1, "and", num2, "is", sum)
