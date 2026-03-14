a,b=map(int,input().split())
k=0
for i in range (a):
    c,d=map(int,input().split())
    k+=(d-c)+1
print( (b-k % b) % b)