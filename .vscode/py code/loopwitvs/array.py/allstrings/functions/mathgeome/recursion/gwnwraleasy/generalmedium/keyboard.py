a=str(input())
s=input().strip()
q=["qwertyuiopasdfghjkl;zxcvbnm,./"]
if a=="R":
    for i in s:
        print(q[0][q[0].index(i)-1],end="")
else:
    for i in s:
        print(q[0][q[0].index(i)+1],end="")