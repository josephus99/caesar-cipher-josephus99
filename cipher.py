def caesar_cipher(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text:
        if char.islower():
            index = (alphabet.index(char) + shift) % 26
            encrypted_text += alphabet[index]
        else:
            encrypted_text += char

    return encrypted_text

def main():
    plain_text = input("Enter a plain text sentence: ").lower()
    shift = 5
    encrypted_text = caesar_cipher(plain_text, shift)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
