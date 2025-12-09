n=int(input())
y=list(map(int,input().split()))
k=-1
for e in y:
    k+=1
    if e<=10:
        
        print("A[{}] = {}".format(k,e))
