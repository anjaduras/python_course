"""Hi! Got inspired to do some zodiac programs.
I'm planning to do this in a couple of steps:
1st: Write a snippet that says "The __ day of the year is this month." (done)
2nd: Snippet saying "This is this exact day of this month." (trying now)
3rd: converts date to zodiac.
"""


def get_month_from_day(day, is_leap_year=False):
    # Define month lengths for a common year
    month_days = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }

    if is_leap_year:
        month_days["February"] = 29

    current_day = 0
    for month, days in month_days.items():
        current_day += days
        if day <= current_day:
            return f"{day} day of {month}"

    # If the day doesn't fall within any month, return an error message
    return "Invalid day or month configuration"


year_day = input("What day of the year is it?: ")
is_it_leap = input("Is it leap year? (yes/no): ").lower()

try:
    day = int(year_day)
    if is_it_leap not in ("yes", "no"):
        print("Error: Please enter yes or no for leap year.")
        exit()
    is_leap_year = is_it_leap == "yes"  # Convert yes/no to boolean
except ValueError:
    print("Error: Please enter a valid number for the day of the year.")
    exit()

month = get_month_from_day(day, is_leap_year)
print(f"Day {day} falls in {month}.")

day_of_year_message = get_month_from_day(day, is_leap_year)
print(day_of_year_message)

# rewriting tomorrow with vlad's suggestions
