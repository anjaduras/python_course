# Exercize 1: Number to Text Transcription
def number_to_text(number):
    number_transcription = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

    if 0 <= number <= 9:
        return number_transcription[number]
    else:
        return "Choose a number between 0 and 9"


number = 7
text = number_to_text(number)
print(f"{number} in text is: {text}")


# Exercize 2: Month number to Text Transcription
def month_num_to_text(number):
    month_transcription = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    if 0 <= number <= 9:
        return month_transcription[number]
    else:
        return "Choose a number between 1 and 12"


number = 2
text = month_num_to_text(number)
if number == 1:
    print(f"{number}st month of the year is called {text}")
elif number == 2:
    print(f"{number}nd month of the year is called {text}")
elif number == 3:
    print(f"{number}rd month of the year is called {text}")
elif 4 <= number <= 12:    
    print(f"{number}th month of the year is called {text}")
else:
    print("Choose a number must between 1 and 12")