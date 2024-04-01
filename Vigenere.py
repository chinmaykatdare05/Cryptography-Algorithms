# Vigenère Cipher


def vigenere_transform(text, key, operation):
    text = text.upper()
    key = key.upper()
    result = []

    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord("A")
            if operation == "encrypt":
                transformed_char = chr(((ord(char) - ord("A") + shift) % 26) + ord("A"))
            else:  # operation == 'decrypt'
                transformed_char = chr(((ord(char) - ord("A") - shift) % 26) + ord("A"))
            result.append(transformed_char)
            key_index = (key_index + 1) % len(key)
        else:
            result.append(char)

    return "".join(result)


print("\nVigenère Cipher\n")
choice = input("0. Encrypt\n1. Decrypt\nEnter your choice: ")
if choice == "0":
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the keyword: ")
    ciphertext = vigenere_transform(plaintext, key, "encrypt")
    print("Encrypted text:", ciphertext)

elif choice == "1":
    ciphertext = input("Enter the ciphertext: ")
    key = input("Enter the keyword: ")
    decrypted_text = vigenere_transform(ciphertext, key, "decrypt")
    print("Decrypted text:", decrypted_text)

else:
    print("Invalid choice. Please choose either 1 or 2.")


# # Solve the given example and perform encryption using Vigenere cipher.
# def vigenere_encrypt(plaintext, key):
#     plaintext, key = plaintext.upper(), key.upper()
#     result = ""
#     key_index = 0
#     for i in plaintext:
#         if i.isalpha():
#             shift = ord(key[key_index]) - 65
#             transformed_char = chr(((ord(i) - 65 + shift) % 26) + 65)
#             result += transformed_char
#             key_index = (key_index + 1) % len(key)
#         else:
#             result += i
#     return result


# plaintext = input("Enter the plaintext: ")
# key = input("Enter the keyword: ")
# print("Encrypted text:", vigenere_encrypt(plaintext, key))


# # Solve the given example and perform decryption using Vigenere cipher.
# def vigenere_decrypt(ciphertext, key):
#     ciphertext, key = ciphertext.lower(), key.lower()
#     result = ""
#     key_index = 0
#     for i in ciphertext:
#         if i.isalpha():
#             shift = ord(key[key_index]) - 97
#             transformed_char = chr(((ord(i) - 97 - shift) % 26) + 97)
#             result += transformed_char
#             key_index = (key_index + 1) % len(key)
#         else:
#             result += i
#     return result


# ciphertext = input("Enter the ciphertext: ")
# key = input("Enter the keyword: ")
# print("Decrypted text:", vigenere_decrypt(ciphertext, key))