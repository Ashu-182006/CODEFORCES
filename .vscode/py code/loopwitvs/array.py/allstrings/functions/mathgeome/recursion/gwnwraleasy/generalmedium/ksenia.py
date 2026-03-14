a,b=map(str,input().split("|"))
c=str(input())
if len(a)>len(b):
    print(a+"|"+b+c)
elif len(a)<len(b):
    print(a+c+"|"+b)
else:
    print("impossible")