def mod_exp(base, exponent, mod):
    """Perform modular exponentiation using binary exponentiation."""
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent >> 1  # Divide exponent by 2
        base = (base * base) % mod  # Square base and reduce modulo
    return result

def generate_keys(q, alpha, XA, XB):
    YA = mod_exp(alpha, XA, q)
    YB = mod_exp(alpha, XB, q)

    private_key_A = mod_exp(YB, XA, q)
    private_key_B = mod_exp(YA, XB, q)

    return YA, YB, private_key_A, private_key_B

def main():    
    q = int(input("Enter a prime number q: "))
    alpha = int(input("Enter a primitive root α: "))
    XA = int(input("Enter Alice's private key XA: "))
    XB = int(input("Enter Bob's private key XB: "))

    YA, YB, private_key_A, private_key_B = generate_keys(q, alpha, XA, XB)

    print("\nPublic keys:")
    print("Public Key for Alice (YA):", YA)
    print("Public Key for Bob (YB):", YB)

    print("\nPrivate keys:")
    print("Private Key for Alice:", private_key_A)
    print("Private Key for Bob:", private_key_B)

if __name__ == "__main__":
    main()
