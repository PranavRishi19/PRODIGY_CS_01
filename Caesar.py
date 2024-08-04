def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Welcome to the Caesar Cipher Program!")
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? Enter E or D (or Q to quit): ").upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice in ['E', 'D']:
            message = input("Enter your message: ")
            try:
                shift = int(input("Enter the shift value (integer): "))
                if choice == 'E':
                    encrypted_message = caesar_cipher_encrypt(message, shift)
                    print(f"Encrypted Message: {encrypted_message}")
                elif choice == 'D':
                    decrypted_message = caesar_cipher_decrypt(message, shift)
                    print(f"Decrypted Message: {decrypted_message}")
            except ValueError:
                print("Invalid input. Please enter an integer for the shift value.")
        else:
            print("Invalid choice. Please enter E, D, or Q.")

if __name__ == "__main__":
    main()
