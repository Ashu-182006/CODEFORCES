n=int(input())
for i in range( n):
    v=0
    l=list(map(int,input().split()))
    for j in l:
        if j>l[0]:
            v+=1
    print(v)
    
