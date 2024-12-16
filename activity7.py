#conditional statements
gold = 0
miner = input("Hi, Please enter your name ---> ")
#answerable by yes or no
hasMine = input("Did you mine gold today? ")

if hasMine.lower()== "yes":
	gold += 1
	print(f"Hi {miner}, Today you have total of {gold} gold")
elif hasMine.lower() == "no":
	gold -= 1
	print(f"Hi {miner}, Today you have total of {gold} gold")
else:
	print(f"Hi {miner}, Today you have total of {gold} gold, try again")
