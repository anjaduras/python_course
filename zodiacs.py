#Hi! Got inspired to do some zodiac programs.
#Im planning to do this in a couple of steps:
#1st: write a snippet that sais that the __ day
#of the year is this month.
#2nd: snippet saying that this is this exact day of this month.
#3rd: no user input, but converts date to zodiac
#4th: user input.

#First Step:
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
      "December": 31
  }

  if is_leap_year:
    month_days["February"] = 29

  current_day = 0
  for month, days in month_days.items():
    current_day += days
    if day <= current_day:
      return month

  # If the day doesn't fall within any month (shouldn't happen), 
  #return an error message
  return "Invalid day or month configuration"

# Example usage (common year)
day = 20
month = get_month_from_day(day)
print(f"Day {day} falls in {month}.")

# Example usage (leap year)
day = 60  # February 29th in a leap year
month = get_month_from_day(day, is_leap_year=True)
print(f"Day {day} falls in {month} (leap year).")
