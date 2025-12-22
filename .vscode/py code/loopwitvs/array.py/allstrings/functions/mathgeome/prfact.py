n=int(input())
i=2
a=[]
while n>1:
    p=1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            p=0
            break
    if p==1:
        while n%i==0:
            a.append(i)
            n//=i
    i+=1
h=0
for i in a:
    h+=1
    if h!=1:
        print("*",end="")
    print ("({}^{})".format(i,a.count(i)),end="")
    