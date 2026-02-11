def revpy(x,i=1):
    if x==0:
        return
    print(((2*x)-1)*"*")
    if x!=1:
        print(i*" ",end="")
    return(revpy(x-1,i+1))
s=int(input())
revpy(s)