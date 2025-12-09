a=int(input())
j=1
for i in range(1,(a*4)+1):
    if i==4*j:
        print("PUM")
        j+=1
    else:
        print(i,end=" ")
    
