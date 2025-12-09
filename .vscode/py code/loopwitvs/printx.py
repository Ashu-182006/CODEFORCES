n=int(input())
j=0
k=n-1

for i in range(n):
    for m in range(n):
        if i==m and j==k:
            print("X",end="")
        else:
            if m==j:
                print('\\',end="")
           
            if m==k:
                print('/',end="")
            if m!=k and m!=j:
                print("*",end="")
    j+=1   
    k-=1     
    print()