# n=int(input())
# l=list(map(int,input().split()))
# for i in range(n):

#     if (i+1)<n :
#         if l[i+1]>0 and l[i] >0 :
#             c=(l[i+1]-l[i])
#         else:
#             c=abs(l[i+1]-l[i])
#     if  l[i-1]>0 and l[i]>0 :
#         d=(l[i]-l[i-1])
#     else:
#         d=abs(l[i]-l[i-1])
#     print(min(c,d),end=" ")
#     if l[i]>0 and l[n-1]>0:
#         a=(l[n-1]-l[i])
#     else:
#         a=abs(l[n-1]-l[i])
#     if l[i]>0 and l[0]>0:
#         b=l[i]-l[0]
#     else:
#         b=abs(l[i]-l[0])
#     print(max(a,b))
n = int(input())
x = list(map(int, input().split()))

for i in range(n):
    if i == 0:
        mini = abs(x[1] - x[0])
    elif i == n - 1:
        mini = abs(x[n-1] - x[n-2])
    else:
        mini = min(abs(x[i] - x[i-1]), abs(x[i+1] - x[i]))
    
    maxi = max(abs(x[i] - x[0]), abs(x[n-1] - x[i]))
    print(mini, maxi)