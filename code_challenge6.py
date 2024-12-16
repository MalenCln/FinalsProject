<<<<<<< HEAD
prelims = eval(input("Enter your Prelims score: "))
midterm = eval(input("Enter your Midterm score: "))
semi = eval(input("Enter your Semifinal score: "))
final  = eval(input("Enter your Finals score: "))
quiz = eval(input("Enter your Quiz scores: "))
project = eval(input("Enter your Project scores: "))

FG = (prelims * 0.15) + (midterm * 0.15) + (semi * 0.15) + (final * 0.15) + (quiz * 0.25) + (project * 0.15)
print("Your Final Grades is", round(FG, 2))


if 65 <= FG <= 100:
	print("You've passed")
	print("great job!")
elif FG >= 64:
	print("Failed")
	print("Better luck next time")
else:
	print("Invalid grades")
=======
prelims = eval(input("Enter your Prelims score: "))
midterm = eval(input("Enter your Midterm score: "))
semi = eval(input("Enter your Semifinal score: "))
final  = eval(input("Enter your Finals score: "))
quiz = eval(input("Enter your Quiz scores: "))
project = eval(input("Enter your Project scores: "))

FG = (prelims * 0.15) + (midterm * 0.15) + (semi * 0.15) + (final * 0.15) + (quiz * 0.25) + (project * 0.15)
print("Your Final Grades is", round(FG, 2))


if 65 <= FG <= 100:
	print("You've passed")
	print("great job!")
elif FG >= 64:
	print("Failed")
	print("Better luck next time")
else:
	print("Invalid grades")
>>>>>>> 41c002e0846cbfe99df7dfbe5626739aaeacf2a5
