a=float(input())
if(a%1==0):
    print("int {}".format(int(a)))
else:
    b=int((a*1000-(a*1000%1000))//1000)
    c=int(a*1000%1000)
    print("float {} 0.{}".format(b,c))