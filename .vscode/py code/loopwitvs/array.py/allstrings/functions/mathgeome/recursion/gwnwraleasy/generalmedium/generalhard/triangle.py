def right(x1, y1, x2, y2, x3, y3):
    def dot(xa, ya, xb, yb):
        return xa * xb + ya * yb
    
    # Check non-degenerate (area != 0)
    area = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
    if area == 0:
        return False
    
    # vectors
    AB = (x2 - x1, y2 - y1)
    AC = (x3 - x1, y3 - y1)
    BA = (x1 - x2, y1 - y2)
    BC = (x3 - x2, y3 - y2)
    CA = (x1 - x3, y1 - y3)
    CB = (x2 - x3, y2 - y3)
    
    return (dot(*AB, *AC) == 0 or
            dot(*BA, *BC) == 0 or
            dot(*CA, *CB) == 0)


x1, y1, x2, y2, x3, y3 = map(int, input().split())

if right(x1, y1, x2, y2, x3, y3):
    print("RIGHT")
else:
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    found = False
    for dx, dy in dirs:
        if right(x1+dx, y1+dy, x2, y2, x3, y3): found = True
        if right(x1, y1, x2+dx, y2+dy, x3, y3): found = True
        if right(x1, y1, x2, y2, x3+dx, y3+dy): found = True
    if found:
        print("ALMOST")
    else:
        print("NEITHER")