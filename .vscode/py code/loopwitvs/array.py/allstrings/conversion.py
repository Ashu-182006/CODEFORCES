a=input()
b=[]
for i in a:
    if i==',':
        b.append(" ")
    else:
        if  65 <= ord(i) <= 90:
            i=ord(i)+32
            b.append(chr(i))
        else:
            i=ord(i)-32
            b.append(chr(i))
print(*b,sep="")