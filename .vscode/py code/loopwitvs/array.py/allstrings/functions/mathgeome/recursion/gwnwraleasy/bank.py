n = input().strip()
num = int(n)

if num >= 0:
    print(num)
else:

    o = int(n[:-1])
 
    p = int(n[:-2] + n[-1])
    print(max(num, o, p))