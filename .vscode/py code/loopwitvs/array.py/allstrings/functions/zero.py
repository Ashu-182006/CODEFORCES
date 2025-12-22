def zero(x):
    for i in range(len(x)):
        if x[i]==0:
             x=[x[-1]]+x[:-1]
    print(*(reversed(x)),sep=' ')
n=int(input())
a=list(map(int,input().split()))
zero(a)