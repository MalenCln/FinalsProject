DLL = input("Are you a current student of DLL (yes/no): ")
if DLL.lower() == "yes":
	print("Welcome to DLL scholarship form")
	CC = input("Are you from Brgy. Cotta? (yes/no): ")
	if CC.lower() == "yes":
		print("Please fill up the next form")
		level = input("What is your current year level right now in DLL\nF - Freshmen\nS - Sophomore\nJ - Junior\nR - Senior\nPlease input your answer: ")
		if level.lower() == 'f' :
			print("Hi, Freshmen")
		elif level.lower() == 's' :
			print("Hi, Sophomore")
		elif level.lower() == 'j' :
			print("Hi, Junior")
		elif level.lower() == 'r' :
			print("Hi, Senior")
		else:
			print("Invalid Answer")
		scho = input("Do you need this scholarship (yes/no) : ")
		if scho.lower() == "yes":
			print("Scholarship Granted")
		else:
			print("Thank you for stopping by")
	else:
		print("Sorry, this scholarship is available only for residents of Cotta")
else:
	print("Thank you for stopping by")