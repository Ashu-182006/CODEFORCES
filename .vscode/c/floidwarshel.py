k=int(input("Enter the number of edges "))
m=int(input("Enter the number of vertix "))
vertix=[]
cost=[]
for i in range(k):
    a=input("enter adjacent vertices  ").strip()
    n=int(input("enter the cost  "))
    vertix.append(a)
    cost.append(n)
for l in range(m):
    l=chr(l+65)
    for j in range(len(m)):
        if 