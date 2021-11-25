alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


def encrypt(text, shift):
    cipher_text = ""
    for i in text:
        cipher_text = cipher_text + \
            alphabet[(alphabet.index(i) + shift) % len(alphabet)]
    print(f'The encoded text is: {cipher_text}')


if direction == 'encode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(decode_text, shift_num):
    decipher_text = ""
    for i in decode_text:
        decipher_text = decipher_text + \
            alphabet[(alphabet.index(i) - shift_num) % len(alphabet)]
    print(f'The decoded text is: {decipher_text}')
  # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  # e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  # print output: "The decoded text is hello"


if direction == 'decode':
    decode_text = input('What is the message you want to decode?\n')
    shift_num = int(input('What is the shift number?\n'))
    decrypt(decode_text, shift_num)

# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
