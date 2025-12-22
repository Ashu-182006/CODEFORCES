roads={"Home":{"market":4,"college":6},
       "market":{"college":2},
       "college":{}}
h={"Home":6,"market":2,"office":0,"college":0}
def best (start,end):
    cost=0
    curent=start
    while curent!=end:
        next_place=min(roads[curent],key=lambda x:roads[curent][x]+h[x])
        cost+=roads[curent][next_place]
        curent=next_place
        print("moving to",curent)
    print("total distance",cost)
best("Home","college")