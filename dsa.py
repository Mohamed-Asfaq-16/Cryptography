# Digital Signature Standard

# 1. Key Generation
p = int(input("Enter prime p: "))
q = int(input("Enter prime q (divides p-1): "))
h = int(input("Enter h (1 < h < p-1): "))
x = int(input("Enter private key x (1 < x < q): "))
hm = int(input("Enter h(m) [message hash value]: "))
k = int(input("Enter random k (1 < k < q): "))


g = pow(h, (p - 1) // q, p)
print("g = ",g)
y = pow(g, x, p)
print("Public key (y) = ", y)
print("Private key (x) = ", x)

# 2. Signature Generation
r = pow(g, k, p) % q
print("R is : ", r)
k_inv = pow(k, -1, q)  # modular inverse of k mod q
s = (k_inv * (hm + x * r)) % q
print("S is : ", s)
print("Signature: (", r, ",", s, ")")

# 3. Signature Verification
print("\n--- Verification ---")
w = pow(s, -1, q)
u1 = (hm * w) % q
u2 = (r * w) % q
v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

if v == r:
    print("Signature is VALID")
else:
    print("Signature is INVALID")
