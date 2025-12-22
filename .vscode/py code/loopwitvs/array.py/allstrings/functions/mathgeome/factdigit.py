def factd(a):
    i=1
    v=0
    while a!=0:
        i=i*a
        a-=1
    while i!=0:
        i//=10
        v+=1
    return(v)
n=int(input())
print("Number of digits of {}! is {}".format(n,factd(n)))