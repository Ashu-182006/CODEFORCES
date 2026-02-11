a,b=map(int,input().split())
if a%2==0:
    for i in range (0,(a//2)):
        print("#"*b,end="\n")
        if i%2!=0:
            print("#",end="")
            print("."*(b-1),end="\n")
        else:
            print("."*(b-1),end="")
            print("#",end="\n")
        i+=2
else:
    for i in range (0,(a//2)+1):
        print("#"*b,end="\n")
        i+=1   
        if i>(a//2):
            break
        if i%2==0:
            print("#",end="")
            print("."*(b-1),end="\n")
        else:
            print("."*(b-1),end="")
            print("#",end="\n")
   