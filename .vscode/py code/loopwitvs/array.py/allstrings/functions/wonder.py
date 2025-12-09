def wonder(a):
    b=(format((a),'b'))
    if b==(b[::-1]) and a%2!=0:
        print("YES")
    else:
        print("NO")       
a=int(input())
wonder(a)