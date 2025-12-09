n=int(input())
a=n
s=0
while n>0:
    r=n%10
    n=n//10
    s=(s*10)+r
print(s)
if a==s:
    print("YES") 
else:
    print("NO")