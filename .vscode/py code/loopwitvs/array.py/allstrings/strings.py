a=input()
b=input()
print(len(a),end=" ")
print(len(b))
print(a+b)
for i in range(len(a)):
    if i==0:
        print(b[i],end="")
    else:
        if i!=len(a)-1:
            print(a[i],end="")
        else:
            print(a[i],end=" ")
for i in range(len(b)):
    if i==0:
        print(a[i],end="")
    else:
        if i!=len(a)-1:
            print(b[i],end="")
        else:
            print(b[i],end=" ")
