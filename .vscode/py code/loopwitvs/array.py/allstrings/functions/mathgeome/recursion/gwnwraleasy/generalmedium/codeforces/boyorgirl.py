n=input().strip()
f="".join(dict.fromkeys(n))
if len(f)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
