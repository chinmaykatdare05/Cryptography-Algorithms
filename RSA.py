# RSA key generation and encryption
p, q, e = map(int, input("Enter values of p, q, e: ").split())
n = p * q
phi_n = (p - 1) * (q - 1)
print("Value of n:", n)
print("Value of phi(n):", phi_n)
M = int(input("Enter Message: "))
C = int(pow(M, e, n))
print("Public key (e, n):", (e, n))
print("Ciphertext:", C)


# # RSA key generation and decryption
# p, q, e = map(int, input("Enter values of p, q, e: ").split())
# n = p * q
# phi_n = (p - 1) * (q - 1)
# print("Value of n:", n)
# print("Value of phi(n):", phi_n)
# C = int(input("Enter Ciphertext: "))
# for i in range(phi_n):
#     if (e * i) % phi_n == 1:
#         d = i
# print("Private key (d, n):", (d, n))
# M = int(pow(C, d) % n)
# print("Message:", M)
