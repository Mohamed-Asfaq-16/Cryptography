def encrypt_caesar(plaintext, key):
    ciphertext = ""
    for char in plaintext:
      start = ord('a')
      shifted_char_code = (ord(char) - start + key) % 26 + start
      ciphertext += chr(shifted_char_code)
    return ciphertext

print(encrypt_caesar("asfaq", 1))

def decrypt_ceasar(ciphertext,key):
  return(encrypt_caesar(ciphertext,-key))

print(decrypt_ceasar("bcd",1))

def bruteforce(ciphertext):
  for key in range(1,26):
    print(decrypt_ceasar(ciphertext,key))

bruteforce("btgbr")

def frequencyanalysis(ciphertext):
    # 1. Count letter frequencies
    counts = {}
    for char in ciphertext:
        counts[char] = counts.get(char, 0) + 1
    # 2. Find the most common letter
    most_common_char = max(counts, key=counts.get)
    print(most_common_char)

    # 3. Calculate the shift (key)
    # The most common letter in English is 'e'
    key = (ord(most_common_char) - ord('e')) % 26
    print(decrypt_ceasar(ciphertext,key))

frequencyanalysis("gggbbb")
