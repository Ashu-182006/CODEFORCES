import math
a,b=input().split()
a=int(a)
b=int(b)
print( "floor {} / {} =".format(a,b),math.floor(a/b))
print( "ceil {} / {} =".format(a,b),math.ceil(a/b))
print( "round {} / {} =".format(a,b).format(a, b), int(a/b + 0.5) if a/b > 0 else int(a/b - 0.5))

