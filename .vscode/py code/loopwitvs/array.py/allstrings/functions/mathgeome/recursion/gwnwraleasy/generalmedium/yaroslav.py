n=int(input())
s=list(map(int,input().split()))
t=list(set(s))
if len(t)==len(s):
    print("YES")
elif(len(s)%2==0):
    if (len(t)>len(s)//2):
        print("yes")
    else:
        print("NO")
else:
    if (len(t)>=(len(s)//2)-1):
        print("YES")
    else:
        print("NO")
