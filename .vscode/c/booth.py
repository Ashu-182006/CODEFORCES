def ARS(A, Q, Q1):
    s = A + Q + Q1
    k = s[0] + s[:-1]
    w = len(A)  
    return k[:w], k[w:2*w], k[2*w]
def add(c, d):
    length = max(len(c), len(d))
    a = reversed(c.zfill(length))
    b = reversed(d.zfill(length))
    result = []
    carry = 0
    for i, j in zip(a, b):
        s = int(i) + int(j) + carry
        result.append(str(s % 2))
        carry = s // 2
    if carry:
        result.append("1")
    return "".join(reversed(result)).zfill(length)[-length:]
def negative(b, a):
    inverted = ''.join('1' if bit == '0' else '0' for bit in a)
    twos_comp = add(inverted, '1'.zfill(len(a)))
    return add(b, twos_comp)
m,n=map(int,input().split())
w = max(m.bit_length(), n.bit_length()) + 1 
Q = bin(m)[2:].zfill(w)
M = bin(n)[2:].zfill(w)
A = "0" * w
Q1 = "0"
for i in range(w):
    if Q[-1] == Q1:   
        A, Q, Q1 = ARS(A, Q, Q1)
    elif Q1 == "0":
        A = negative(A, M)
        A, Q, Q1 = ARS(A, Q, Q1)
    else:
        A = add(A, M)
        A, Q, Q1 = ARS(A, Q, Q1)
h=str(A)+str(Q)
print(h+"=",end=" ")
print(int(h,2))


