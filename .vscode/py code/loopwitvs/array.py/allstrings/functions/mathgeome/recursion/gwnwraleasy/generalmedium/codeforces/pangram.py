import string

n = int(input())
s = input().strip().lower() 
if all(ch in s for ch in string.ascii_lowercase):
    print("YES")
else:
    print("NO")
