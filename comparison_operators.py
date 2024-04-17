# Exersize 1: Check the Range
def is_in_range(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound


number = 15
lower_bound = 10
upper_bound = 100
if is_in_range(number, lower_bound, upper_bound):
    print(f"{number} is within the range {lower_bound} to {upper_bound}")
else:
    print(f"{number} is not within the range {lower_bound} to {upper_bound}")


# Exercize 2: Grade Check
def check_grade(score):
    if score >= 90:
        return "1"
    elif score >= 85:
        return "2"
    elif score >= 70:
        return "3"
    elif score >= 60:
        return "4"
    else:
        return "Nicht bestanden!"


score = 85
grade = check_grade(score)
if score >= 60:
    print(f"Dein Ergebniss {score} entspricht der Note {grade}")
else:
    print(f"Nicht bestanden!")
