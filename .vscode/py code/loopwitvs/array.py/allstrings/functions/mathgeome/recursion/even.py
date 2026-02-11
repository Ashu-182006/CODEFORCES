def even (a):
    if len(a)%2==0:
        print(*a[len(a)-2::-2])
    else:
        print(*a[::-2])
a=int(input())
s=list(map(int,input().split()))
even(s)