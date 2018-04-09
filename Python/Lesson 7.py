import random

gameWon = False
secret = random.randrange(1,100)
lives = 5
# keep going while the game has not been won
while not gameWon and lives >0:
    guess = int(input("Enter a number "))
    # see if they were close or not!
    diff = guess - secret
    # diff could be negative!
    if diff < 0:
        diff = diff * -1
    # ensure that guess is within 20
    if guess > secret and diff <= 20:
            print ("guess is too big")
    elif guess < secret and diff <=20:
            print ("guess is too small")
    elif guess == secret:
            print ("Well done you guessed correctly!")
            gameWon = True
    else:
      print ("Your nowhere near!")
    lives = lives - 1
    print ("you have ", str(lives), " left")

# has the game been won?
if(not gameWon):
    print ("You have lost. Bow your head in shame! The number was ", secret)
