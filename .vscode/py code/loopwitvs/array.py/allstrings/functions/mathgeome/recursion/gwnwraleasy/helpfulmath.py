s = input().strip()
n= list(map(int, s.split('+')))
n.sort()
print('+'.join(map(str, n)))