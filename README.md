# Caesar Cipher

![Caesar Cipher](https://example.com/your-image-url.jpg) <!-- Replace with an actual image URL if you have one -->

## Overview

The Caesar Cipher is a type of substitution cipher in which each letter in the plaintext is shifted a fixed number of places down the alphabet. It is named after Julius Caesar, who reportedly used it to communicate with his officials. The Caesar Cipher is one of the simplest and most widely known encryption techniques.

## How It Works

In the Caesar Cipher, each letter of the plaintext is shifted to a certain number of positions to the right or left in the alphabet. For example, with a shift of 3, 'A' would be replaced by 'D', 'B' would become 'E', and so on. This shift is consistent for all letters in the plaintext.

### Example

- **Plaintext**: `HELLO`
- **Shift**: `3`
- **Ciphertext**: `KHOOR`

In the example above, each letter of the plaintext `HELLO` is shifted three positions to the right to produce the ciphertext `KHOOR`.

## Decryption

Decryption of a Caesar Cipher text involves shifting the letters back in the opposite direction. Using the same shift value used for encryption, the ciphertext can be converted back to the original plaintext.

### Example

- **Ciphertext**: `KHOOR`
- **Shift**: `3`
- **Plaintext**: `HELLO`

## Implementation

The Caesar Cipher can be implemented in various programming languages with simple logic. Here is a basic example in Python:

```python
def encrypt(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Example usage
plaintext = "HELLO"
shift = 3
ciphertext = encrypt(plaintext, shift)
print(f"Ciphertext: {ciphertext}")

decrypted_text = decrypt(ciphertext, shift)
print(f"Decrypted Text: {decrypted_text}")
