a=[]
n = int(input())
for i in range(n):
    x=int(input())
    while(x>0):
        x=x*(x-1)
        x-=1
    a.append(x)
print(a)