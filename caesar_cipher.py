def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isupper():
            plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            plaintext += char
    return plaintext

def main():
    print(" CIPHER-SHIELD: Basic Encryption & Decryption ")
    while True:
        print("\n1. Encrypt\n2. Decrypt\n3. Exit")
        choice = input("Enter Choice: ")
        if choice == '1':
            text = input("Enter Plaintext: ")
            shift = int(input("Enter Shift Key 1-25: "))
            encrypted = encrypt(text, shift)
            print(f"\nCiphertext: {encrypted}")
            print(f"Validation: {decrypt(encrypted, shift)}")
        elif choice == '2':
            text = input("Enter Ciphertext: ")
            shift = int(input("Enter Shift Key 1-25: "))
            print(f"\nPlaintext: {decrypt(text, shift)}")
        elif choice == '3': break

if __name__ == "__main__":
    main()
