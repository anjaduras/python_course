#Exercize: Number to Text Transcription
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
    return "Choose a number must between 0 and 9)"

number = 7
text = number_to_text(number)
print(f"{number} in text is: {text}")
