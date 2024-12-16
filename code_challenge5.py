<<<<<<< HEAD
pera = eval(input("Enter amount to deposit ---> "))
name = input("Enter your name: ")

libo = pera // 1000
lsukli = pera % 1000
fh = lsukli // 500
fhsukli = lsukli % 500
th = fhsukli//200
thsukli = fhsukli % 200
oh = thsukli//100
ohsukli = thsukli % 100
fif = ohsukli//50
fifsukli = ohsukli % 50
tw = fifsukli//20
twsukli = fifsukli % 20
t = twsukli//10
tsukli = twsukli % 10
f = tsukli//5
fsukli = tsukli % 5
o = fsukli//1
osukli = fsukli % 1

print(f"Hi {name} the breakdown of your deposit is")
print(libo, " - 1000")
print(fh, " - 500")
print(th, " - 200")
print(oh," - 100")
print(fif," - 50")
print(tw," - 20")
print(t," - 10")
print(f," - 5")
print(o," - 1")
=======
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
>>>>>>> 41c002e0846cbfe99df7dfbe5626739aaeacf2a5
