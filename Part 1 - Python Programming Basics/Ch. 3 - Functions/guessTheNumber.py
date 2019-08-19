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
        break   # If the guess is neither higher nor lower than the secret number it must be equal to it
                # in which case you want the program execution to break out of the for loop


if guess == secretNumber:
    print("Good job! You guessed my secret number in {} guesses!".format(guessesTaken))
else:
    print("Nope, the number I was thinking of was {}".format(secretNumber))
    