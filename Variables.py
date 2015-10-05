name = input("Hi there. Whats your name? ")
age = input("Hi " + name + ". How old are you? ")
print ("Hi " + name + ". You are " + age + ".")
correct = input("Is that right? ")
if correct is ["yes", "Yes", "Yep", "yep", "correct", "Correct", "Right", "right", "true", "True"]:
	print("Yay, I was right")
else:
	print("Awww, I got it wrong")
