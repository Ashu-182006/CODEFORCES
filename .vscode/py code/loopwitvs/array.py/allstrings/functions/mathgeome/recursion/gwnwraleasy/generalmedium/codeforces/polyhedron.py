n=int(input())
f=0
for i in range(n):
    polyhedron = input().strip()
    if polyhedron == "Tetrahedron":
        f += 4
    elif polyhedron == "Cube":
        f += 6
    elif polyhedron == "Octahedron":
        f += 8
    elif polyhedron == "Dodecahedron":
        f += 12
    elif polyhedron == "Icosahedron":
        f += 20
print(f)