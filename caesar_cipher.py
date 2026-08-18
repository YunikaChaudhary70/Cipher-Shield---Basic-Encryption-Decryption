# CIPHER-SHIELD: Basic Encryption & Decryption
# Project 2 - DecodeLab Internship
# Algorithm: Caesar Cipher

def encrypt(plaintext, shift):
    """Encrypt text using Caesar Cipher"""
    ciphertext = ""
    shift = shift % 26  # Handle shift > 26
    
    for char in plaintext:
        if char.isupper():
            # Formula: E(x) = (x + n) % 26
            ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Handle spaces and punctuation
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    """Decrypt text using Caesar Cipher"""
    plaintext = ""
    shift = shift % 26  # Handle shift > 26
    
    for char in ciphertext:
        if char.isupper():
            # Formula: D(x) = (x - n) % 26
            plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            # Handle spaces and punctuation
            plaintext += char
    return plaintext

def main():
    print("="*50)
    print("    CIPHER-SHIELD: Basic Encryption & Decryption")
    print("="*50)
    
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt") 
        print("3. Exit")
        
        choice = input("\nEnter Choice: ")
        
        if choice == '1':
            text = input("Enter Plaintext: ")
            shift = int(input("Enter Shift Key 1-25: "))
            encrypted = encrypt(text, shift)
            print(f"\n[ENCRYPTED]: {encrypted}")
            print(f"[VALIDATION]: {decrypt(encrypted, shift)}")  # Proof that it works
        
        elif choice == '2':
            text = input("Enter Ciphertext: ")
            shift = int(input("Enter Shift Key 1-25: "))
            decrypted = decrypt(text, shift)
            print(f"\n[DECRYPTED]: {decrypted}")
            
        elif choice == '3':
            print("Exiting CIPHER-SHIELD. Stay Secure!")
            break
            
        else:
            print("Invalid Choice! Please enter 1, 2 or 3")

if __name__ == "__main__":
    main()
