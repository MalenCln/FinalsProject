
# def add(num1, num2):
#     print(f"the sum of {num1} and {num2} is {x}")
#     num1 + num2 = x
#     return x

# def sub(num1, num2):
#     print(f"the difference of {num1} and {num2} is {x}")
#     x = num1 - num2
#     return

# add("32", "4")

#grocery
# nameCustomer = input("Enter the customer's name :  ")
# ageCustomer = eval(input("Enter the customer's age : "))
# dGrocery = input("Did you buy a grocery? [yes/no] : ")

# if dGrocery.lower() == "yes":
#     print("\n\t\t\tWelcome, enjoy buying groceries!")
#     item = input("What item did you buy? :  ")
#     price_item = float(input("How much is the item? :   "))
#     money = float(input("How much do you like to pay? :   "))
    
#     if ageCustomer >= 60:
#         taxed = price_item + (price_item * 0.123)
#         total = taxed
#         change = money - total
#         discount = taxed * 0.052
#         isDiscounted = total - discount
#         changeD = money - isDiscounted 
#         print("You can have senior discount of 5.2% from the total price." )
#         print(f"Hi, {nameCustomer}, you purchased {item} with the a price of {price_item} plus 12.3% taxed {taxed} minus 5.2% total discount. \nTotal : {isDiscounted} \nAmount Given : {money} \nChange : {round(changeD,2)}")
        
#     elif ageCustomer <= 59:
#         taxed = price_item + (price_item * 0.123)
#         total = taxed
#         change = money - total
#         print("You are ineligible for the senior discount.")
#         print(f"Hi, {nameCustomer}, you purchased {item} with the price of {price_item} plus 12.3% tax {taxed}. \nTotal : {total} \nAmount Given: {money} \nChange : {round(change,2)}")
# else:
#     print("Thank you for coming! ")


a = input('Did you buy an item from the store?("yes or no"): ')

price = 250
aprice = price + (12.3 / 100) * price
ap = aprice - (5.2 / 100) * aprice

if a.lower() == "yes":
	print ('Name of the item: Coke') 
	print ('Price of the item: '  ,price,)
	amount = eval(input('Total of amount given: '))

	age = int(input('What is your age: '))

	if age >= 60:
		print("")
		print (f"Total Price: {price}, Plus 12.3% Tax")
		print ('Total: ' , aprice,)
		print (' You will get a discount of 5.2%, your total purchase is ', ap,)

	elif age <=59:
		print ("The total amount of you purchase is", aprice,)
else:
	print ('Please buy our productssssssss')