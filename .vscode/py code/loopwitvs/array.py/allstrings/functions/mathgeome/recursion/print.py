def printf( x):
    if x==0:
        return 
    print("I love Recursion")
    return (printf(x-1))
x=int(input())
printf(x)