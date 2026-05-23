def merge(a,b):
    k=[]
    k.append(a)
    k.append(b)
    return k
def perge(d,m):
    for i in d:
        if i[1]>m:
            d.remove(i)
        else:
            for j in d[i+1::]:
                if i[0]==j[0] and i[1]==j[1]:
                    d.remove(j)
                elif i[0]>j[0] and j[1]>i[1]:
                    d.remove(j)
                elif i[0]>j[0] and j[1]<i[1]:
                    d.remove(i)
                elif i[0]>j[0] and i[1]==j[1]:
                    d.remove(j)
                elif i[0]==j[0] and j[1]<i[1]:
                    d.remove(j)
s=list(map(int,input("Enter the profit: ").split()))
