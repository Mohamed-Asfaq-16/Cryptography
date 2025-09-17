def xtime(a):
    return (((a<<1)^0x1B)& 0xFF) if (a & 0x80 ) else (a<<1)

def mult(a,b):
    res = 0
    for i in range(8):
        if (b&1):
            res ^= a
        b>>=1
        a = xtime(a)
    return res & 0xFF

def inverse(a):
    if a == 0:
        return 0
    for i in range(1,256):
        if mult(i,a)==1:
            return i
    return 0
def affine(a):
    c = 0x63
    y = 0
    for i in range(8):
        bit = ((a>>i) & 1) ^ ((a>> ((i+4)%8)) & 1) ^ ((a>> ((i+5)%8)) & 1) ^ ((a>> ((i+6)%8)) & 1) ^((a>> ((i+7)%8)) & 1) ^ (( c>>i)&1)
        y |= (bit<<i)
    return y & 0xFF

def sbox(a):
    return affine(inverse(a))

def rotate(a):
    return a[1:]+a[:1]

def substitute(a):
    return [sbox(x) for x in a]

rcons = [ 0x01 , 0x02 ,0x04 , 0x08 , 0x10 , 0x20 , 0x40 , 0x80 , 0x1b , 0x36 ]

nk = 4
nb = 4
nr = 10
key = eval(input())
w = [list(key[i:i+4]) for i in range(0, len(key), 4)]
for i in range(nk , nb * (nr + 1)):
    temp = w[i-1]
    if i % nk == 0:
        temp = substitute(rotate(temp))
        temp[0] ^= rcons[(i//nk)-1]
    w.append([a^b for a,b in zip(temp,w[i-nk])])
for i in range(11):
    print(f"Round {i} :", w[4*i: (4*i)+4])