def arrayaverage(a):
    if len(a)==0:
        return 0
    return (a[0]+arrayaverage(a[1:])*len(a[1:]))/len(a)
n=int(input())

s=list(map(int,input().split()))
print(f"{arrayaverage(s):.6f}")