a=input().strip().lower()
b=input().strip().lower()
l=g=0
for i in range(len(a)):
    if a[i]!=b[i]:
        if ord(a[i])>ord(b[i]):
            l+=1
        else:
            g+=1
if l>g:
    print(1)
elif g>l:
    print(-1)
else:
    print(0)