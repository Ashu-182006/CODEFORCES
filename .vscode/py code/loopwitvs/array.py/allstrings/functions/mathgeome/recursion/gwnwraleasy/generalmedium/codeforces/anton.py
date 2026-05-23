s = input().strip("{}")
if not s:
    print(0)
else:
    i = list(map(str.strip, s.split(",")))
    print(len(set(i)))
