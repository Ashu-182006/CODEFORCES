def printf(x):
    i=1
    while i!=x+1:
        if i==x:
            print(i,end="")
        else:
            print(i,end=" ")
        i+=1
n=int(input())
printf(n)
