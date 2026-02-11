def printn(n):
    if n==0:
        return
    if n!=1:
        print(n,end=" ")
    else:
        print(n,end="")
    return(printn(n-1))
s=int(input())
printn(s)