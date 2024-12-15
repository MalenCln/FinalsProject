def pang_hello():
    print("Hello BSIT-1C")
pang_hello()

#with paraneter

def pang_hello2(name):
    print(f"Hello {name}!")
pang_hello2("malen")


tuloy = True
while tuloy == True:
    ask = input("Please input your name ---> ")
    if ask.lower() == "stop":
        print("Program stopped")
        print("Thank you!")
        break
    else:
        pang_hello2(ask)
    

        





