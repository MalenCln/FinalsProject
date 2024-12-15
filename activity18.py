tri = eval(input("Enter numbers of triangles: "))

for x in range(1,6):
    for r in range(1,tri +1):
        for y in range(1, x + 1):
            print("*", end = " ")
        for z in range(5, x, -1):
            print(" ", end=" ")
    print()