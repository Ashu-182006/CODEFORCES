a=int(input())


if a%8==0 or a%8==7:
    c=0
    b=-1
    i=0
    while i<=a:
        b+=1       
        if i==a:
            break
        else:
            if i%8==0:
                i=i+7
            else:
                i+=1

    
elif a%8==1 or a%8==6:
    c=1
    i=1
    b=-1
    while i<=a:
        b+=1
        if i==a:
            break
        else:
            if i%8==1:
                i=i+5
            else:
                i+=3
      

elif a%8==2 or a%8==5:
    c=2
    i=2
    b=-1
    while i<=a:
        b+=1
        if i==a:
            break
        else:
            if i%8==2:
                i=i+3
            else:
                i+=5

elif a%8==3 or a%8==4:
    c=3
    b=-1
    i=3
    while i<=a:
        b+=1
        if i==a:
            break
        else:
            if i%8==4:
                i=i+7
            else:      
                i+=1
print(b,c)