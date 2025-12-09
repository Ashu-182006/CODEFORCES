def power(x,y):
    s=0
    for i in range(2,y+1,2):
        
        s=s+x**i
    print(s)
a,b=map(int,input().split())
power(a,b)