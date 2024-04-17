# Exercize 1: Leap Year Calculator
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False


year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# Exercize 2: Converting Minutes to Hours
def convert_minutes_to_hours(total_minutes):

    hours = total_minutes // 60  # Integer division to get hours
    minutes = total_minutes % 60  # Modulo to get remaining minutes
    return f"{hours} hour{('s' if hours > 1 else '')} {minutes} minute{('s' if minutes > 1 else '')}"


# Example usage
total_minutes = 113
time_str = convert_minutes_to_hours(total_minutes)
print(f"{total_minutes} minutes is equal to {time_str}")
