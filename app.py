alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def encrypt(text: str, shift: int) -> str:
    encrypted_text = ""

    for letter in text:
        if letter not in alphabet:
            encrypted_text += letter
            continue
        position = alphabet.index(letter)
        if position + shift > len(alphabet):
            encrypted_text += alphabet[position + shift - len(alphabet)]
        else:
            encrypted_text += alphabet[position + shift]
    return encrypted_text


def decrypt(text: str, shift: int) -> str:
    encrypted_text = ""

    for letter in text:
        if letter not in alphabet:
            encrypted_text += letter
            continue
        position = alphabet.index(letter)
        encrypted_text += alphabet[position - shift]
    return encrypted_text


if __name__ == "__main__":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        print(encrypt(text, shift))
    elif direction == "decode":
        print(decrypt(text, shift))
