while True:
    a,b =map(int,input().split())
    sum=0
    
    if a<=0 or b<=0 :
        break
    elif a>b:
        for i in range(b,a+1):
            sum+=i
            print(i,end=" ")        
    else:
        for i in range(a,b+1):
            sum+=i
            print(i,end=" ") 
    print(f"sum ={sum}")