from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)  # Create a DES cipher object
    padded_plaintext = pad(plaintext.encode(), DES.block_size)  # Pad plaintext
    ciphertext = cipher.encrypt(padded_plaintext)  # Encrypt padded plaintext
    return ciphertext

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)  # Create a DES cipher object
    padded_plaintext = cipher.decrypt(ciphertext)  # Decrypt ciphertext
    plaintext = unpad(padded_plaintext, DES.block_size).decode()  # Unpad and decode
    return plaintext

def main():
    # Define a key (must be exactly 8 bytes for DES)
    plaintext = input('Enter Plaintext: ')
    key = b'abcdefgh'
    print('Key:', key)
    
    ciphertext = des_encrypt(plaintext, key)
    print(f"\nCiphertext (hex): {ciphertext.hex()}")

    decrypted_text = des_decrypt(ciphertext, key)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
