# Exercise 1: Area of a Rectangle
length = 5
width = 3
area = length * width
print(f"The area of the rectangle is {area} square meters.")

# Exercise 2: Discount Calculation
original_price = 13.00
discount_percent = 0.10
discount_amount = original_price * discount_percent
final_price = original_price - discount_amount  
print(
    f"After a {discount_percent * 100:.0f}% discount, the final price is ${final_price:.2f}"
)

#Exercise 3: Coin Change Calculator
amount = 175 
euro_value = 100  # 1 euro in cents
fifty_cent_value = 50
twenty_cent_value = 20
ten_cent_value = 10
five_cent_value = 5
one_cent_value = 1

num_euros = amount // euro_value
remaining_amount = amount % euro_value

num_fifty_cent = remaining_amount // fifty_cent_value
remaining_amount = remaining_amount % fifty_cent_value

num_twenty_cent = remaining_amount // twenty_cent_value
remaining_amount = remaining_amount % twenty_cent_value

num_ten_cent = remaining_amount // ten_cent_value
remaining_amount = remaining_amount % ten_cent_value

num_five_cent = remaining_amount // five_cent_value
remaining_amount = remaining_amount % five_cent_value

num_one_cent = remaining_amount

print(f"{amount} cents can be made up of:")
print(f"{num_euros} euro coins")
print(f"{num_fifty_cent} fifty cent coins")
print(f"{num_twenty_cent} twenty cent coins")
print(f"{num_ten_cent} ten cent coins")
print(f"{num_five_cent} five cent coins")
print(f"{num_one_cent} one cent coins")
#to-do: try to connect this exersize with user input.

#Exercise 4: Percent Calculator
def calculate_percentage(number1, number2):
  percentage = (number2 / number1) * 100
  return percentage
number1 = 286
number2 = 59
percentage = calculate_percentage(number1, number2)
print(f"{number2} is {percentage:.0f}% of {number1}.")
