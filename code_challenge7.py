name = input("Enter your name: ")
age = input("Enter your age: ")
gro = input("Do you want to buy? (yes or no): ")
if gro.lower() == "yes":
    print("\nHERE IS THE LIST OF OUR PRODUCTS: \n\tEggs - ₱220 \n\tChicken Meat - ₱200 \n\tRice - ₱190 \n\tButter - ₱55 \n\tMilk - ₱165 \n\tBread - ₱90 \n\tCereal - ₱192")
    item = input("What item would you like to buy? ")
    price = input("Input the price of the item: ")
    amount = input("Enter the amount you'd like to pay: ")

    if age >= 60:
        taxed = price + (price * 0.123)
        total = taxed
        change = amount - total
        disc = taxed * 0.052
        total_disc = total - disc
        change = amount - total_disc 
        print("You can have senior discount of 5.2% from the total price." )

    elif age < 60:
        print

else:
    print("Thanks for stopping buy!")