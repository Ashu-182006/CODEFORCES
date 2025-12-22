def concat(x,y):
    z=x+y
    print(*z,sep=' ')
a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
concat(c,b)