a=input()
b=int(input())
y = list(map(int, input().split()))
for i in y:
    while i>0:
        if i==1:
            print(a)
        else:
            print(a, end='')
        i-=1