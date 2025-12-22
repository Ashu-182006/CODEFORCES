def fact(a):
    i=1
    while a!=0:
        i=i*a
        a-=1
    return(i)
a,b=map(int,input().split())
print(int(fact(a)/(fact(b)*fact(a-b))),end=" ")
print(int(fact(a)/fact(a-b)),end="")