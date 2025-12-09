y=[]
p=0
a,b=map(int,input().split())
p=0
for i in range (a):
    
    c=list(map(int,input().split()))
    y.append(c)
d=int(input())
for i in y:
     if d in i:
          print("will not take number")
          p=1
          break
if p==0:
     print("will take number")    
