import math

lowercase_alphabets = "abcdefghijklmnopqrstuvwxyz"

def modinv(a, m=26):
    try:
        return pow(a, -1, m)
    except ValueError:
        return None

def pad_text(text, size):
    n = len(text) % size
    if n != 0:
        text += 'x' * (size - n)
    return text.lower()

def text_to_matrix(text, size):
    cols = len(text) // size
    matrix = [[0] * cols for _ in range(size)]
    for i in range(cols):
        for j in range(size):
            matrix[j][i] = lowercase_alphabets.index(text[i * size + j])
    return matrix

def matrix_to_text(matrix, size):
    cols = len(matrix[0])
    text = ""
    for i in range(cols):
        for j in range(size):
            matrix[j][i] %= 26
            text += lowercase_alphabets[matrix[j][i]]
    return text

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for c in range(n):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1)**c) * matrix[0][c] * determinant(minor)
    return det


def cofactor_matrix(matrix, mod=26):
    n = len(matrix)
    cofactors = []
    for r in range(n):
        cofactor_row = []
        for c in range(n):
            minor = [row[:c] + row[c+1:] for i, row in enumerate(matrix) if i != r]
            cofactor = ((-1)**(r+c)) * determinant(minor)
            cofactor_row.append(cofactor % mod)
        cofactors.append(cofactor_row)
    return cofactors

def matrix_mod_inverse(matrix, mod=26):
    n = len(matrix)
    det_val = determinant(matrix) % mod
    if det_val == 0:
        return None
    det_inv = modinv(det_val, mod)
    if det_inv is None:
        return None

    cofactors = cofactor_matrix(matrix, mod)
    adjugate = [[cofactors[c][r] for c in range(n)] for r in range(n)]
    inverse = [[(det_inv * adjugate[r][c]) % mod for c in range(n)] for r in range(n)]
    return inverse

def matmul(A, B, mod=26):
    rows, cols, inner = len(A), len(B[0]), len(B)
    result = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(inner):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= mod
    return result

def encrypt(pt, size, key):
    pt1 = pad_text(pt, size)
    ptmatrix = text_to_matrix(pt1, size)
    ctmatrix = matmul(key, ptmatrix)
    return matrix_to_text(ctmatrix, size)

def decrypt(ct, size, key):
    ctmatrix = text_to_matrix(ct.lower(), size)
    inv_key = matrix_mod_inverse(key)
    if inv_key is None:
        return None
    ptmatrix = matmul(inv_key, ctmatrix)
    return matrix_to_text(ptmatrix, size)

def known(pt, ct, size):
    if len(pt) < size*size or len(ct) < size*size:
        print("Invalid: insufficient length")
        return None
    max_shifts = len(pt) - size*size + 1
    for shift in range(max_shifts):
        pt_block = pt[shift:shift + size*size]
        ct_block = ct[shift:shift + size*size]
        ptmatrix = text_to_matrix(pt_block, size)
        ctmatrix = text_to_matrix(ct_block, size)
        pt_inv = matrix_mod_inverse(ptmatrix)
        if pt_inv is not None:
            key = matmul(ctmatrix, pt_inv)
            return key

    print("No valid invertible block found")
    return None

if __name__ == "__main__":
    key = [[9, 2], [1, 5]]

    ct = encrypt("hello", 2, key)
    print("Cipher text:", ct)

    pt = decrypt(ct, 2, key)
    print("Decrypted text:", pt)

    k = known(pt,ct,2)
    print(k)
