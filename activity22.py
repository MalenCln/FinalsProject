import os
act = True
while act == True:
    ask = input("Would you like to see activity 5? (yes/no)---> ")
    if ask.lower() == "yes":
        os.system("cls")
        number1 = eval(input("Enter a number ---> "))
        number2 = eval(input("Enter another number ---> "))
        answer = number1 + number2
        print("The sum of", number1, "and", number2, "is", answer)
        continue
    else:
        print("Program stopped")
        break
