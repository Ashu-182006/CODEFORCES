n = int(input())
s = list(map(int, input().split()))[1:]  # skip count
d = list(map(int, input().split()))[1:]  # skip count
k = set(s + d)

if len(k) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
