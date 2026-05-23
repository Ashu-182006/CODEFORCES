a, b, h = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(a)]

r = list(range(a))
c = list(range(b))

for _ in range(h):
    x, y, z = input().split()
    y, z = int(y) - 1, int(z) - 1

    if x == "g":
        print(l[r[y]][c[z]])
    elif x == "r":
        r[y], r[z] = r[z], r[y]
    elif x == "c":
        c[y], c[z] = c[z], c[y]
# a, b, h = map(int, input().split())
# l = [list(map(int, input().split())) for _ in range(a)]

# for _ in range(h):
#     x, y, z = input().split()
#     y, z = int(y)-1, int(z)-1 

#     if x == "g":
#         print(l[y][z])

#     elif x == "r": 
#         l[y], l[z] = l[z], l[y]

#     elif x == "c": 
#         for i in range(a):
#             l[i][y], l[i][z] = l[i][z], l[i][y]

# a,b,h=map(int,input().split())
# u=[]
# l=[list(map(int,input().split())) for i in range(a)]
# for i in range(h):
#     x,y,z=map(str,input().split())
#     if x=="g":
#         print(l[int(y)-1][int(z)-1])
#     elif x=="r":
#         for i in range(a):
#             u.append(l[int(y)-1][(i)])
#             l[int(y)-1][i]=l[int(z)-1][i]
#             l[int(z)-1][i]=u[i]
#         u.clear()
#     elif x=="c":
#         for  i in range(b):
#             u.append(l[i][int(y)-1])
#             l[i][int(y)-1]=l[i][int(z)-1]
#             l[i][int(z)-1]=u[i]
#         u.clear()
# print(l)