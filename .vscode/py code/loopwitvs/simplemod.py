n=int(input())
a=1
b=1
while a<=10**9 and b<=10**9:
    if ((a**2)*(b**2))%n==0:
        print(a,b)
        break
    else:
        if a<=b:
            a+=1
        else:
            b+=1
else:
    print("No solution")