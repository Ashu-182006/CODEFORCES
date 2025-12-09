a,b,c=input().split()
a=int(a)
b=(b)
c=int(c)
if b=='=':
    if a==c:
        print("Right")
    else:
        print("Wrong")
if b=='>':    
    if a>c:
        print("Right")
    else:
        print("Wrong")
if b=='<'        :
    if a<c:
        print("Right")
    else:
        print("Wrong")