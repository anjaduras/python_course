"""Hi! Got inspired to do some zodiac programs.
I'm planning to do this in a couple of steps:
1st: Write a snippet that says "The __ day of the year is this month." (Already done)
2nd: Snippet saying "This is this exact day of this month." (Implemented here)
3rd: No user input, but converts date to zodiac.
4th: User input.
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
            # Calculate day within the month (considering 1-based indexing)
            day_of_month = day - current_day + 1
            # Format the output string with ordinal suffix (st, nd, rd, th)
            ordinal_suffix = "th"
            if day_of_month % 10 == 1 and day_of_month != 11:
                ordinal_suffix = "st"
            elif day_of_month % 10 == 2 and day_of_month != 12:
                ordinal_suffix = "nd"
            elif day_of_month % 10 == 3 and day_of_month != 13:
                ordinal_suffix = "rd"
            return f"{day}{ordinal_suffix} day of {month}"

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

# Determine month based on day and leap year
month = get_month_from_day(day, is_leap_year)
print(f"Day {day} falls in {month}.")


# Get the formatted result from the function
day_of_year_message = get_month_from_day(day, is_leap_year)

# Print the result
print(day_of_year_message)