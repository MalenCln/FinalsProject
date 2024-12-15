#factorial
x = 1
num = eval(input("Enter a number: "))
for fm in range(num,0,-1): 
    x *= fm
print(f"The factorial of {num} is {x}")