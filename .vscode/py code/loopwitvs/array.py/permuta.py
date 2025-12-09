n=int(input())
y=(list(map(int,input().split())))
z=(list(map(int,input().split())))
i=list(set(y)&set(z))
if len(i)==len(set(y))  or len(i)==len(set(z)):
    print("yes")
else:
    print("no")