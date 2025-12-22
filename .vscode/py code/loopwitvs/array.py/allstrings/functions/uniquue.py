def unique(x):
    x=set(x)
    print(len(x))
n=int(input())
a=list(map(int,input().split()))
unique(a)