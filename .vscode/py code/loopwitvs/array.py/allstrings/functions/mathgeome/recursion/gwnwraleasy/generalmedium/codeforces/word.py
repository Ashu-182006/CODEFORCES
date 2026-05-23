a=input().strip()
s=0
for i in a:
    if i.isupper():
        s+=1
if s>len(a)//2:
    print(a.upper())
else:
    print(a.lower())