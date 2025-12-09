s=input()
if "+" in s:
    a,b = s.split('+')
    a=int(a)
    b=int(b)
    print(a+b)
elif "-" in s:
    a,b=s.split('-')
    a=int(a)
    b=int(b)
    print(a-b)
elif "*" in s:
    a,b =s.split('*')
    a=int(a)
    b=int(b)
    print(a*b)
elif "/" in s:
    a,b =s.split('/')
    a=int(a)
    b=int(b)
    print(a//b)