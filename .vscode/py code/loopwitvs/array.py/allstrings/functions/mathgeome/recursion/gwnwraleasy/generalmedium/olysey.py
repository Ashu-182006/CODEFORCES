a,b=map(int,input().split())
for i in range( (10**(a-1)),(10**a)):
    if "0" not in str(i):
        if i%b==0:
            print(i)
            break
