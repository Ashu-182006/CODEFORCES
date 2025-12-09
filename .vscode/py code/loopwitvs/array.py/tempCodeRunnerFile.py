y=[]
p=0
a,b=map(int,input().split())
for j in range(a):
     y.append(list(map(int, input().split()))) 
c=int(input())
for j in range (a):
    for i in y[j]:
        if i==c:
            p=1
            print("will not take number")
if p==0:
    print("will take number")           