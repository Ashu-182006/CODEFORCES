a=input()
a,b =[int(i) for i in str(a)]
if a==0 or b==0:
    print("YES")
else:
    print("YES" if a%b==0 or b%a==0 else ("NO"))