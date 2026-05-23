a, b = input().split("|")
c = input()

L, R, U = len(a), len(b), len(c)
total = L + R + U

if total % 2 != 0:   # odd total → impossible
    print("Impossible")
else:
    target = total // 2
    if L > target or R > target:
        print("Impossible")
    else:
        need_left = target - L
        need_right = target - R
        if need_left + need_right != U:
            print("Impossible")
        else:
            print(a + c[:need_left] + "|" + b + c[need_left:])