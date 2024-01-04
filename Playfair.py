# Playfair Cipher


def generate_square_key(key):
    key = key.replace("J", "I").upper()  # Replace J with I and convert to uppercase
    key_set = set(key)  # Convert to set to remove duplicate characters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    remaining_chars = [char for char in alphabet if char not in key_set]
    matrix_string = key + "".join(remaining_chars)
    square_key = [matrix_string[i : i + 5] for i in range(0, 25, 5)]
    return square_key


def find_char(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)
    return None, None


def find_char(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)
    return None, None


def playfair_cipher(text, key, option):
    square_key = generate_square_key(key)
    processed_text = []

    # Prepare the text by grouping characters
    i = 0
    while i < len(text):
        if i == len(text) - 1 or text[i] == text[i + 1]:
            processed_text.append(text[i] + "Z")
            i += 1
        else:
            processed_text.append(text[i] + text[i + 1])
            i += 2

    result = []
    for pair in processed_text:
        char1, char2 = pair[0], pair[1]
        row1, col1 = find_char(square_key, char1)
        row2, col2 = find_char(square_key, char2)

        if row1 is None or row2 is None:
            result.append(pair)
            continue

        shift = 1 if option == "0" else -1
        if row1 == row2:
            result.append(
                square_key[row1][(col1 + shift) % 5]
                + square_key[row2][(col2 + shift) % 5]
            )
        elif col1 == col2:
            result.append(
                square_key[(row1 + shift) % 5][col1]
                + square_key[(row2 + shift) % 5][col2]
            )
        else:
            result.append(square_key[row1][col2] + square_key[row2][col1])

    return square_key, "".join(result)


def main():
    text = input("Enter text: ")
    key = input("Enter the key: ")
    option = input("Enter 0 to encrypt or 1 to decrypt: ")
    square_key, result = playfair_cipher(text, key, option)
    print("Key Matrix:")
    for row in square_key:
        print(row)
    if option == "0":
        print("Encrypted Text:", result)
    elif option == "1":
        print("Decrypted Text:", result)


if __name__ == "__main__":
    main()


# # Solve the given example. Generate a key matrix and perform encryption using Playfair cipher.
# def generate_key_square(key):
#     key = key.replace(" ", "").upper().replace("J", "I")
#     alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
#     key_square = ""

#     for char in key + alphabet:
#         if char not in key_square:
#             key_square += char
#     return key_square


# def encrypt(plaintext, key):
#     key_square = generate_key_square(key)
#     plaintext = plaintext.replace(" ", "").upper().replace("J", "I")
#     ciphertext = ""
#     index = 0

#     while index < len(plaintext):
#         if index == len(plaintext) - 1:
#             pair = plaintext[index] + "X"
#         elif plaintext[index] == plaintext[index + 1]:
#             pair = plaintext[index] + "X"
#         else:
#             pair = plaintext[index] + plaintext[index + 1]
#             index += 1

#         row1, col1 = divmod(key_square.index(pair[0]), 5)
#         row2, col2 = divmod(key_square.index(pair[1]), 5)

#         if row1 == row2:
#             col1 = (col1 + 1) % 5
#             col2 = (col2 + 1) % 5
#         elif col1 == col2:
#             row1 = (row1 + 1) % 5
#             row2 = (row2 + 1) % 5
#         else:
#             col1, col2 = col2, col1

#         ciphertext += key_square[row1 * 5 + col1] + key_square[row2 * 5 + col2]
#         index += 1
#     return key_square, ciphertext


# plaintext = input("Enter the plaintext: ")
# key = input("Enter the key: ")
# key_square, ciphertext = encrypt(plaintext, key)
# print("Key Square:")
# for i in range(0, 25, 5):
#     print(" ".join(key_square[i : i + 5]))
# print("\nCiphertext:", ciphertext)


# # Solve the given example. Generate a key matrix and perform decryption using Playfair cipher.
# def generate_key_square(key):
#     key = key.replace(" ", "").upper()
#     alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
#     key_square = ""

#     for char in key:
#         if char not in key_square:
#             key_square += char

#     for char in alphabet:
#         if char not in key_square:
#             key_square += char
#     return key_square


# def decrypt(ciphertext, key):
#     key_square = generate_key_square(key)
#     plaintext = ""
#     index = 0

#     while index < len(ciphertext):
#         pair = ciphertext[index] + ciphertext[index + 1]
#         row1, col1 = divmod(key_square.index(pair[0]), 5)
#         row2, col2 = divmod(key_square.index(pair[1]), 5)

#         if row1 == row2:
#             col1 = (col1 - 1) % 5
#             col2 = (col2 - 1) % 5
#         elif col1 == col2:
#             row1 = (row1 - 1) % 5
#             row2 = (row2 - 1) % 5
#         else:
#             col1, col2 = col2, col1

#         plaintext += key_square[row1 * 5 + col1] + key_square[row2 * 5 + col2]
#         index += 2

#     return plaintext.lower()


# ciphertext = input("Enter the ciphertext: ")
# key = input("Enter the key: ")
# print("Key Square:")
# for i in range(0, 25, 5):
#     print(" ".join(generate_key_square(key)[i : i + 5]))
# print("Plaintext:", decrypt(ciphertext, key))
