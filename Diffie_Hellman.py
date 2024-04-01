# Diffie Hellman

import random


def mod_exp(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent >> 1
        base = (base * base) % mod
    return result


def generate_keys(q, alpha, XA, XB):
    # Calculate YA and YB
    YA = mod_exp(alpha, XA, q)
    YB = mod_exp(alpha, XB, q)

    # Calculate the shared secret key for Alice and Bob
    secret_key_A = mod_exp(YB, XA, q)
    secret_key_B = mod_exp(YA, XB, q)

    return YA, YB, secret_key_A, secret_key_B


q = int(input("Enter the prime number q: "))
alpha = int(input("Enter the primitive root α: "))
XA = int(input("Enter Alice's private key XA: "))
XB = int(input("Enter Bob's private key XB: "))

if XA < 1 or XA >= q or XB < 1 or XB >= q:
    print(f"Invalid private key values. They should be in the range [1, {q}-1].")
    return

YA, YB, secret_key_A, secret_key_B = generate_keys(q, alpha, XA, XB)

print("\nPublic keys:")
print("YA (Alice's public key):", YA)
print("YB (Bob's public key):", YB)

print("\nShared keys:")
print("Shared Key for Alice:", secret_key_A)
print("Shared Key for Bob:", secret_key_B)



# # Implement Diffie Hellman (DH) Key Exchange algorithm. Inputs q, ∝, XA & XB will be given.
# def mod_exp(base, exponent, mod):
#     result = 1
#     base = base % mod
#     while exponent > 0:
#         if exponent % 2 == 1:
#             result = (result * base) % mod
#         exponent = exponent >> 1
#         base = (base * base) % mod
#     return result


# def generate_keys(q, alpha, XA, XB):
#     YA, YB = mod_exp(alpha, XA, q), mod_exp(alpha, XB, q)
#     secret_key_A, secret_key_B = mod_exp(YB, XA, q), mod_exp(YA, XB, q)
#     return YA, YB, secret_key_A, secret_key_B


# q, alpha = map(int, input("Enter the prime number q and primitive root α: ").split())
# XA, XB = map(int, input("Enter Alice and Bob's private key XA and XB: ").split())

# if not 1 <= XA < q or not 1 <= XB < q:
#     print("Private key values should be less than q")
# else:
#     YA, YB, secret_key_A, secret_key_B = generate_keys(q, alpha, XA, XB)
#     print("\nPublic keys:")
#     print("YA (Alice's public key):", YA)
#     print("YB (Bob's public key):", YB)
#     print("\nShared keys:")
#     print("Shared Key for Alice:", secret_key_A)
#     print("Shared Key for Bob:", secret_key_B)