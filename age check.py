#Age Check
print("Welcome to the movie Theatre!!!")
age = input("May I know your age please?: ")
if age:
	age = int(age)
	if age <= 2:
		print("Free entry for infants :) ")
	elif age > 2 and age <= 12:
		print("Child Price")
	elif age < 18:
		print("Adult Price , No Hard driks allowed")
	elif age >= 18:
		print("Adult Price, Drinks Allowed :) ")
else:
	print("Please repeat your age")