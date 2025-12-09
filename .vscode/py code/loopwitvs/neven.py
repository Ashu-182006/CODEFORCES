a=0
b=0
c=0
d=0
n = int(input())
y = list(map(int, input().split()))

for  i in y:
    if i%2==0:
        a+=1
    else:
        b+=1
    if i>=0:
        c+=1
        if i==0:
            c-=1
    else:
        d+=1
print("Even: {}".format(a))
print("Odd: {}".format(b))
print("Positive: {}".format(c))
print("Negative: {}".format(d))