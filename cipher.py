def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    shift = 5
    plain_text = input("Enter the plain text sentence: ")
    encrypted_text = caesar_cipher(plain_text, shift)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()
