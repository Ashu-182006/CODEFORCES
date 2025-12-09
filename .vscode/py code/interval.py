a=float(input())
if(a<0 or a>100):
    print("Out of Intervals")
else:
    for i in range(0,1001,25):
        if(a>i and a<=i+25):
            if(i==0):
                print("Interval [0,25]")
                break
            else:

                 print("Interval ({},{}]".format(i,i+25))
                 break
        elif(a==i):
            print("Interval [{},{}]".format(i-25,i))
            break

