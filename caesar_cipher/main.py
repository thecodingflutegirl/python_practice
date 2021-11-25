from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift):
    coded_text = ""
    for i in text:
        if i in alphabet:
            if direction == 'decode':
                coded_text = coded_text + \
                    alphabet[(alphabet.index(i) - shift) % len(alphabet)]
            else:
                coded_text = coded_text + \
                    alphabet[(alphabet.index(i) + shift) % len(alphabet)]
        else:
            coded_text += i
    print(f"The {direction}d text is : {coded_text}")


please_continue = True
while please_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    restart = input(
        'Would you like to restart the program? Type "yes" if you want to go again. Otherwise type "no"\n').lower()
    if restart == 'no':
        please_continue = False
        print('Thank you, goodbye!')
