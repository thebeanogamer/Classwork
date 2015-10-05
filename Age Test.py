# <0 is fetus
# 0 is newborn
# 1-3 is toddler
# 4-7 is young child
# 8-12 is child
# 13-19 is teen
# 20-59 is adult
# 60 is OAP
# 123< is oldest in world

while True:
	age = int(input("How old are you?"))
	
	if age < 0:
		print ("You are a fetus, congratulations!")
	elif age == 0:
		print ("You are a newborn, congratulations!")
	elif 1 <= age <= 3:
		print ("You are a toddoler, congratulations!")
	elif 4 <= age <= 7:
		print ("You are a young child, congratulations!")
	elif 8 <= age <= 12:
		print ("You are a child, congratulations!")
	elif 13<= age <= 19:
		print ("You are a teenager, congratulations!")
	elif 20 <= age <= 59:
		print ("You are a adult, congratulations!")
	else:
		if 200 <= age:
			print ("You are a liar!")
		elif 123 <= age:
				print ("You are the oldest person ever, congratulations!")
		elif 60 <= age:
			print ("You are a OAP, congratulations!")
