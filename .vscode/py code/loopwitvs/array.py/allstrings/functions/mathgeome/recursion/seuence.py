def sequence(n,a=1):
    if n==1:
        return a
    if n%2==0:
        return sequence(n/2,a+1)
    return sequence((n*3)+1,a+1)
n=int(input())
print(sequence(n))