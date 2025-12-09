y=[]


a=int(input())
for _ in range(a):
    s=(input())
    y.append(s)

for i in y:
    t=int(i)
    p=0
    k=len((i))
    
    while t>0:
        d=t%10
        if d=='':
            print(0,end=' ')
        else:
            print(d,end=' ')  
            p+=1  
        t=t//10
    while k!=p:
        print(0,end=" ")
        p+=1
    k=0

    print()
      