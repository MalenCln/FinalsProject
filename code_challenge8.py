<<<<<<< HEAD
x = 0
odd = 0
even = 0
for fm in range (1,11):
    num = eval(input(f"Input #{fm}: "))
    x += num
    if num % 2 == 0:
        even += num
    else:
        odd += num

print(f"The summation of the numbers is: {x}")
print(f"The summation of the even numbers is: {even}")
=======
x = 0
odd = 0
even = 0
for fm in range (1,11):
    num = eval(input(f"Input #{fm}: "))
    x += num
    if num % 2 == 0:
        even += num
    else:
        odd += num

print(f"The summation of the numbers is: {x}")
print(f"The summation of the even numbers is: {even}")
>>>>>>> 41c002e0846cbfe99df7dfbe5626739aaeacf2a5
print(f"The summation of the odd numbers is: {odd}")