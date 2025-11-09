# Caesar Cipher Implementation

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result


def decrypt(text, shift):
    # simply reverse the shift
    return encrypt(text, -shift)


# --- Main Program ---
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("\nEncrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
