s = input().strip()
if '?' in s:
    s = s.split('?', 1)[1]

u = ""
p = ""
pr = ""
r = ""
k = ""
i = 0

while i < len(s):
    if i+7 < len(s) and s[i:i+9] == "username=": 
        i += 9
        while i < len(s) and s[i] != '&':
            u += s[i]; i += 1
    elif i+3 < len(s) and s[i:i+4] == "pwd=":    
        i += 4
        while i < len(s) and s[i] != '&':
            p += s[i]; i += 1
    elif i+7 < len(s) and s[i:i+8] == "profile=": 
        i += 8
        while i < len(s) and s[i] != '&':
            pr += s[i]; i += 1
    elif i+4 < len(s) and s[i:i+5] == "role=":    
        i += 5
        while i < len(s) and s[i] != '&':
            r += s[i]; i += 1
    elif i+3 < len(s) and s[i:i+4] == "key=":     
        i += 4
        while i < len(s) and s[i] != '&':
            k += s[i]; i += 1
    else:
        i += 1

print("username:", u)
print("pwd:", p)
print("profile:", pr)
print("role:", r)
print("key:", k)