def ra(vertix,weight,n):
    k=0
    for i in vertix:
        if n in i:
            k+=1
    return k
            

def mstgf(k,n):
    k=int(input("Enter the number of edges "))
    m=int(input("Enter the number of stages ")) 
    vertix=[]
    weight=[]
    for i in range(k):
        a=input("enter adjacent vertices in forwar order ").strip()
        n=int(input("enter the weight  "))
        vertix.append(a)
        weight.append(n)

    cost=[]
    cost[n]=0
    for j in range(m-1):
        for i in range(ra(vertix,weight,))
        cost[j]=
        
        
l=str(input("enter the source vertex "))
f=str(input("enter the destination vertex "))
mstgf(l,f)
