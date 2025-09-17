alphabets = 'abcdefghijklmnopqrstuvwxyz'
def key(e,phi):
  d=pow(e,-1,phi)
  return e,d
def stringtonumber(pt):
    return [alphabets.index(c) for c in pt]
def numtostring(numlist):
    return ''.join([alphabets[n] for n in numlist])
def encrypt(pt, e, n):
    nums = stringtonumber(pt)
    cipher = [pow(m, e, n) for m in nums]
    return cipher
def decrypt(cipher, d, n):
    decrypted_nums = [pow(c, d, n) for c in cipher]
    return numtostring(decrypted_nums)
while True:
    print("\n1. Key\n2. Encrypt\n3. Decrypt\n4. Exit")
    choice = int(input())

    if choice == 1:
        p = int(input("Enter P : ").strip())
        q = int(input("Enter q : ").strip())
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537
        if phi % e == 0:
            print("65537 is not coprime with φ(n). Choose another P, Q.")
            continue
        e, d = key(e, phi)
        print("The public key :", e)
        print("The private key :", d)

    elif choice == 2:
        pt = input("Enter the Plaintext: ").lower()
        cipher = encrypt(pt, e, n)
        print("The cipher text is :", cipher)

    elif choice == 3:
        cipher = list(map(int, input("Enter the Ciphertext (space-separated): ").split()))
        try:
            pt = decrypt(cipher, d, n)
            print("The Plaintext is:", pt)
        except Exception as ex:
            print("ERROR!", ex)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid number")