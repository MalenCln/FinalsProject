name = str(input("Enter you name : "))
amount = int(input("Enter amount deposit : "))

thousand = 1000
five_hundred = 500 
two_hundred = 200
one_hundred = 100
fifty = amount = 50
twenty  = 20
ten = 10
five = 5
one = 1
print(f"Hi {name}, the breakdown of your deposit is: ")
flr_div = amount // 1000
fvi = amount % five_hundred

print(flr_div, "1000")

fvi = amount % five_hundred
print(f"{fvi} {five_hundred} ")
print(f"{flr_div} {two_hundred} ")
print(f"{flr_div} {one_hundred} ")
print(f"{flr_div} {fifty} ")
print(f"{flr_div} {ten}")
print(f"{flr_div} {five}")
print(f"{flr_div} {one}")