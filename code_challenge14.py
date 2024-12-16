cycle = True
sum = 0

while cycle == True:
    num = eval(input("Enter a number:   "))

    if num == 0:
        print("Program has been terminated")
        print(f"The sum of all numbers is {sum}")
        break
           
    else:
        sum += num
        continue