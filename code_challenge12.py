for x in range (1,6):
    for y in range(6, x, -1):
        print(" ", end=" ")
    for z in range (1, x):
        print("*", end=" ")
    for a in range (0, x):
        print("*", end=" ")
    print()

for i in range(6,1-1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(7,i -1):
        print("*",end=" ")
    for l in range(6,i -1):
        print("*",end=" ")
    print()

for i in range(1,7):
    for j in range(1,5):
        print(" ",end=" ")
    for k in range(1,4):
        print("*",end=" ")
    print()