a=[]
c=[]
k=0
x=int(input())
for i in range(x):
    y=input()
    for i in range(len(y)):
        for j in range(i,len(y)):
            a.append((y[i:j+1]))
            if y[i:j+1]=="010" or  y[i:j+1]=="101":
                break
    f="101"
    l="010"
    if l in a or f in a:
        c.append("Good")
    else:
        c.append("Bad")
print(*c,sep="\n")