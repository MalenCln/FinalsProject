age = eval(input("Enter your age: "))

if 1 <= age <= 7:
	print("The age you enter is considered as Toddler")
elif 8<= age <= 13:
	print("The age you enter is considered as Pre teen")
elif 14<= age <= 18:
	print("The age you enter is considered as Teenager")
elif 19 <= age <=31:
	print("The age you enter is considered as Early Adulthood")
elif 32 <= age <= 45:
	print("The age you enter is considered as Mid Adulthood")
elif 46 <= age <=59:
	print("The age you enter is considered as Post Adulthood")
elif 60 <= age <= 100:
	print("The age you enter is considered as Senior")
else:
	print("Invalid Age")
