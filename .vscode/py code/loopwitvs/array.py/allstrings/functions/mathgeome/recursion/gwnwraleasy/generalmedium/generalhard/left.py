# a=input().strip()
# b=input().strip()
# if len(a)>=len(b):
#     if b in a:
#         print(len(a)-len(b))
     
#     elif a in b:
#         print(len(b-len(a)))

#     else:
#         for i in range(1,len(b)+1):
#             if b[i:] in a:
#                 print(len(a)-len(b)+i+1)
#                 break
def min_moves(s: str, t: str) -> int:
    i, j = len(s) - 1, len(t) - 1
    common = 0
    while i >= 0 and j >= 0 and s[i] == t[j]:
        common += 1
        i -= 1
        j -= 1
    return (len(s) - common) + (len(t) - common)
s = input().strip()
t = input().strip()
print(min_moves(s, t))