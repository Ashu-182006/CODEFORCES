def count(a):
    if not a:
        return 0
    vowels = 'aeiouAEIOU'
    first, *rest = a
    if first in vowels:
        return 1 + count(rest)
    else:
        return count(rest)
a=list(input().strip())
print(count(a))