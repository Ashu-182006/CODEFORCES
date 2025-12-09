a=input()
b = ord(a)
if  65 <= b <= 90:
    b=b+32
else:
    b=b-32
print(chr(b))