def find(p, n):
    while p[n] != n:
        p[n] = p[p[n]]
        n = p[n]
    return n
k=int(input("Enter the number of edges "))
vertix=[]
cost=[]
for i in range(k):
    a=input("enter adjacent vertices  ").strip()
    n=int(input("enter the cost  "))
    vertix.append(a)
    cost.append(n)
m=0
t = [[0 for i in range(2)] for i in range(k)]

graph = list(zip(vertix, cost))
graph.sort(key=lambda x: x[1])
vertix,cost = zip(*graph)
p = {ch: ch for pair in vertix for ch in pair}
for i in range(k):
    if find(p, vertix[i][0]) != find(p, vertix[i][1]):
        p[find(p, vertix[i][0])] = find(p, vertix[i][1])  
        t[i][0] = vertix[i][0]  
        t[i][1] = vertix[i][1]
        m += cost[i]
print("the minimum cost is ",m)
    