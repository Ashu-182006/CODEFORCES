# a=dict()
# a=dict([(1,'bd'),(2,'gd')])
# a[1]='1234'
# print(a)
# a=dict()
# a=dict([(1,'bd'),(2,'gd')])
# a[4]='124'
# print(a)

# a=dict()
# a=dict([(1,'bd'),(2,'gd')])
# print(a.pop(1))
# print(a)

# a=dict()
# a=dict([(1,'bd'),(2,'gd')])
# print(a.popitem())
# print(a)

# a=dict()
# a=dict([(1,'bd'),(2,'gd')])
# a.clear()
# print(a)

# a ={}.fromkeys(['a','s''d'],0)
# print(a)

# a={2:'er',3:6,4:8}
# print(a.items())

# a={2:'er',3:6,4:8}
# print(a.values())

a={1:1 ,2:2,3:3,4:4}
b={k: v*v for k,v in a.items()}
print(b)