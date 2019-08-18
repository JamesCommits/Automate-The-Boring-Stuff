# This is a guess the number game.
import random
secretNumber = random.randint(1,45)
print("I am thinking of a number between 1 & 45")

# Ask the player to guess six times
for guessesTaken in range(1,7):
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is a little low")
    elif guess > secretNumber:
        print("Your guess is a little high")
    else:
        break   # This runs when they get the correct guess

if guess == secretNumber:
    print("Good job! You guessed my secret number " + str(guessesTaken) + ' guesses!')
    