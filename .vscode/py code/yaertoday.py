a=int(input())
j=0
i=0
if(a>=365):
    while a>=365 :
        a=a-365
        i=i+1
if(a>=30):
    while a>=30 :
        a=a-30
        j=j+1
print("{} years".format(i))
print("{} months".format(j))
print("{} days".format(a))