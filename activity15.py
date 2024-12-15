
# num = eval(input("Enter a number: "))
for x in range(6,0,-1):
    for y in range(1, x + 1):
        print(" ", end=" ")
    for x in range(6,y ,- 1):
        print("*", end=" ")
    print()
        
    
