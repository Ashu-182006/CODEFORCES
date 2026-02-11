n=int(input())
t=0
if n%4==0 or n%7==0:
    print("YES")
else:
    for i in str(n):
        if int(i)==4 or int(i)==7:
            t+=1
    if t==len(str(n)):
        print("YES")
    else:
        print("NO")
        
