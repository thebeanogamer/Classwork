while True:
	distance = int(input("How far is your journey in km?"))

	if distance >= 500 :
		canFly = input("Can you/do you want to fly?")
		if canFly == "Yes" or canFly == "yes":
			print ("Take a plane!")
		else:
			print ("Get on a boat or a coach!")
	else:
		ownCar = input("Do you own a car?")
		if ownCar == "yes" or ownCar == "Yes":
			print ("Drive your car!")
		else:
			print ("Take the train")
