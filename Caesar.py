# Shift (Caesar/Additive) Cipher


def encrypt(plaintext, key):
    return "".join(
        chr((ord(i) - 65 + key) % 26 + 65)
        if "A" <= i <= "Z"
        else chr((ord(i) - 97 + key) % 26 + 97)
        if "a" <= i <= "z"
        else i
        for i in plaintext
    )


def decrypt(ciphertext, key):
    # Decryption is just encryption with the negative key
    return encrypt(ciphertext, -key)


def brute_force_attack(ciphertext):
    possible_plaintexts = []
    for key in range(1, 26):
        plaintext = decrypt(ciphertext, key)
        possible_plaintexts.append((key, plaintext))
    return possible_plaintexts


print("\nImplementation of Shift (Caesar/Additive) Cipher\n")
x = int(input("-1. Brute Force\n0. Encrypt\n1. Decrypt\nEnter your choice: "))

if x == -1:
    ciphertext = input("Enter the ciphertext to decrypt: ")
    possible_plaintexts = brute_force_attack(ciphertext)
    print("\nPossible plaintexts using brute-force attack:")
    for key, plaintext in possible_plaintexts:
        print(f"Key {key}: {plaintext}")

elif x == 0:
    plaintext = input("Enter Plaintext: ")
    key = int(input("Enter key: "))
    encrypted_text = encrypt(plaintext, key)
    print("Encrypted Text:", encrypted_text)

elif x == 1:
    ciphertext = input("Enter Ciphertext: ")
    key = int(input("Enter key: "))
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)


# # Solve the given example and perform encryption using Shift cipher/Substitution/Ceaser cipher.
# def encrypt(plaintext, key):
#     plaintext = plaintext.upper()
#     return "".join(
#         chr((ord(i) - 65 + key) % 26 + 65) if "A" <= i <= "Z" else i for i in plaintext
#     )


# plaintext = input("Enter Plaintext: ")
# key = int(input("Enter key: "))
# print("Encrypted Text: ", encrypt(plaintext, key))


# # Solve the given example and Perform decryption using Shift cipher/Substitution/Ceaser cipher.
# def decrypt(ciphertext, key):
#     ciphertext = ciphertext.lower()
#     return "".join(
#         chr((ord(i) - 97 - key) % 26 + 97) if "a" <= i <= "z" else i for i in ciphertext
#     )


# ciphertext = input("Enter Ciphertext: ")
# key = int(input("Enter key: "))
# print("Decrypted Text:", decrypt(ciphertext, key))
