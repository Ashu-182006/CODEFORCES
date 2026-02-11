def pyra(x,a=1):
    
    if x<a:
        return
    print((x-a)*" ",end="")
    print(((2*a)-1)*"*")
    return(pyra(x,a+1))
x=int(input())
pyra(x)
