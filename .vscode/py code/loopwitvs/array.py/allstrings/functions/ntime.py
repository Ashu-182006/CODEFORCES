def nin(x,y):
    for i in range(int(x)):
        if i==int(x)-1:
            print(y)
        else:
            print(y,end=' ')
n=int(input())
for i in range (n):
    x,y=map(str,input().split())
    nin(x,y)
