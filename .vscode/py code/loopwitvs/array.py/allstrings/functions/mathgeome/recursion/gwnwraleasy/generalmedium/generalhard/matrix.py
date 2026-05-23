def spiral(matrix):
    if not matrix: return
    l=0 
    r=len(matrix[0])-1
    t=0
    b=len(matrix)-1
    while l<=r and t<=b:
        for i in range(l,r+1):
            print(matrix[t][i],end=' ')
        t+=1
        for i in range(t,b+1):
            print(matrix[i][r],end=' ')
        r-=1
        if t<=b:
            for i in range(r,l-1,-1):
                print(matrix[b][i],end=' ')
            b-=1
        if l<=r:
            for i in range(b,t-1,-1):
                print(matrix[i][l],end=' ')
            l+=1
m,n=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(m)]
spiral(matrix)
# def spiral(matrix):
#     if not matrix: return
#     print(*matrix[0],end=" ")
#     spiral(list(zip(*matrix[1:]))[::-1])
# m,n=map(int,input().split())
# matrix=[list(map(int,input().split())) for _ in range(m)]
# spiral(matrix)