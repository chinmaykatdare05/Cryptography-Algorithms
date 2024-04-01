# Digital Signature


def gcd(a, b):
    # Calculate the greatest common divisor (GCD) using Euclidean algorithm
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    # Calculate the extended GCD using recursive Euclidean algorithm
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):
    # Calculate the modular inverse of 'a' modulo 'm' using extended GCD
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("The inverse does not exist.")
    return x % m


def generate_keys(p, q, e):
    # Generate RSA public and private keys
    n = p * q
    phi = (p - 1) * (q - 1)

    if gcd(phi, e) != 1:
        raise ValueError(f"Invalid public exponent {e}")

    d = mod_inverse(e, phi)

    public_key = (e, n)  # Public key consists of the exponent 'e' and modulus 'n'
    private_key = (d, n)  # Private key consists of the exponent 'd' and modulus 'n'

    return public_key, private_key


def sign_message(message, private_key):
    # Generate a digital signature for the message using the private key
    d, n = private_key
    signature = pow(message, d, n)  # Signature = message^d mod n
    return signature


def verify_signature(signature, message, public_key):
    # Verify the digital signature using the public key
    e, n = public_key
    decrypted_signature = pow(signature, e, n)  # Decrypt signature using public key

    if decrypted_signature == message:
        return True  # Signature is valid if decrypted signature matches the original message
    else:
        return False  # Signature is not valid if decrypted signature differs from the original message



# Input prime numbers p, q, and public exponent e from the user
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
e = int(input("Enter public exponent e: "))

# Generate public and private keys using user-provided input
public_key, private_key = generate_keys(p, q, e)
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

# Input the message to be signed
message = int(input("Enter the message: "))

# Generate digital signature using the private key
signature = sign_message(message, private_key)
print("Digital Signature:", signature)

# Input the received signature for verification
received_signature = int(input("Enter the received signature: "))

# Verify the signature using the public key
if verify_signature(received_signature, message, public_key):
    print("The message is authentic.")
else:
    print("The message is altered. Discard.")



# # Implement RSA Digital Signature Scheme. Inputs p, q and e will be given.
# p, q, e = map(int, input("Enter prime numbers p, q and public exponent e: ").split())
# n = p * q
# phi_n = (p - 1) * (q - 1)
# for i in range(phi_n):
#     if (e * i) % phi_n == 1:
#         d = i
# print("Public Key (e, n):", (e, n))
# print("Private Key (d, n):", (d, n))
# M = int(input("Enter the message: "))
# S = int(pow(M, d) % n)
# print("Digital Signature:", S)
# received_signature = int(input("Enter the received signature: "))
# M_dash = int(pow(S, e) % n)
# if received_signature == M_dash:
#     print("The message is authentic.")
# else:
#     print("The message is altered. Discard.")