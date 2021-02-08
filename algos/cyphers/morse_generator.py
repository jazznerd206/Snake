MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    "&": ".-...",
    "@": ".--.-.",
    ":": "---...",
    ",": "--..--",
    ".": ".-.-.-",
    "'": ".----.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    # Exclamation mark is not in ITU-R recommendation
    "!": "-.-.--",
}


def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            cipher += "/ "

    # Remove trailing space added on line 64
    return cipher[:-1]


def decrypt(message):
    decipher = ""
    letters = message.split(" ")
    for letter in letters:
        if letter != "/":
            decipher += list(MORSE_CODE_DICT.keys())[
                list(MORSE_CODE_DICT.values()).index(letter)
            ]
        else:
            decipher += " "

    return decipher

print(encrypt('THIS IS A STRING'))
print(encrypt('THIS IS LIBRARY'))
print(encrypt('THIS IS THE END OF THE WORLD AS WE KNOW IT'))

print(decrypt('- .... .. ... / .. ... / .- / ... - .-. .. -. --.'))
print(decrypt('- .... .. ... / .. ... / .-.. .. -... .-. .- .-. -.--'))
print(decrypt('- .... .. ... / .. ... / - .... . / . -. -.. / --- ..-. / - .... . / .-- --- .-. .-.. -.. / .- ... / .-- . / -.- -. --- .-- / .. -'))

