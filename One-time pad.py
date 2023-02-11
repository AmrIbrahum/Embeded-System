from random import randint

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def generate_otp(characters):
    with open("otp.txt", "w") as f:
        for i in range(characters):
            f.write(str(randint(0, 26)) + "\n")


def load_otp():
    with open("otp.txt", "r") as f:
        contents = f.read().splitlines()
    return contents


def encrypt(message, key):
    ciphertext = ''
    for (position, character) in enumerate(message):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) +
                         int(key[position])) % len(ALPHABET)
            ciphertext += ALPHABET[encrypted]
    return ciphertext


while True:
    message = input("Please enter a message: ")
    if message == "q":
        break
    generate_otp(len(message))
    positive_keys = load_otp()
    negative_keys = [-1*int(i) for i in positive_keys]

    encry_message = encrypt(message, positive_keys)
    decry_message = encrypt(encry_message, negative_keys)

    print("Encrypted message: ", encry_message)
    # print(positive_keys)
    # print(negative_keys)
    print("decrypted message: ", decry_message)