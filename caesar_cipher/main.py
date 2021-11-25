alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(direction, text, shift):
    coded_text = ""
    for i in text:
        position = alphabet.index(i)
        if direction == 'decode':
            coded_text = coded_text + \
                alphabet[(alphabet.index(i) - shift) % len(alphabet)]
        else:
            coded_text = coded_text + \
                alphabet[(alphabet.index(i) + shift) % len(alphabet)]
    print(f"The {direction}d text is : {coded_text}")


caesar(direction, text, shift)

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
