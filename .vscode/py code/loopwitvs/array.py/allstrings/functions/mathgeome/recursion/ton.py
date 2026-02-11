def printn(n,a=1):
    if a>n:
        return
    print(a)
    return(printn(n,a+1))
s=int(input())
printn(s)