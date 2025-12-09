n=int(input())
b=[]
for i in range (n):
    a=input()
    if len(a)>10:
        b.append(str(a[0])+str(len(a)-2)+str(a[len(a)-1]))
    else:
        b.append(a)
print(*b,sep="\n")