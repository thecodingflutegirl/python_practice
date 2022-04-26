from ascii import logo, goodbye
from code_dictionaries import letters, numbers, punctuation

print(logo)

converter_on = True


def morse_code_converter(split_string, string_input):
    morse_texts = []
    for item in split_string:
        coded_word = ""
        for i in item:
            if i in letters:
                coded_word = coded_word + letters[i] + " "
            elif i in numbers:
                coded_word = coded_word + numbers[i] + " "
            elif i in punctuation:
                coded_word = coded_word + punctuation[i] + " "
            else:
                print(
                    f"Unable to translate '{i}'.\nThis character is not part of the morse code dictionary or symbols.")
        morse_texts.append(coded_word)
    coded_sentence = "/".join(morse_texts)
    print(f"'{string_input.lower()}' in morse code is: \n{coded_sentence}")


while converter_on:
    string_input = input(
        "Enter a string to convert into morse code \nType 'quit' to stop.\n: ").upper()
    if string_input == "QUIT":
        print(goodbye)
        break

    split_string = string_input.split(" ")

    morse_code_converter(split_string, string_input)

    restart = input(
        "Would you like to convert anything else?\nType 'yes' or 'no': ").lower()
    if restart == 'no':
        converter_on = False
        print(goodbye)
