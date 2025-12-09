a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a%c==0 and b%c==0:
    print("Both")
if a%c==0 and b%c!=0:
    print("Memo")
if a%c!=0 and b%c==0:
    print("Momo")
if a%c!=0 and b%c!=0:
    print("No One")