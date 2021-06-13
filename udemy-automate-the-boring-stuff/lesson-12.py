# This is a guess the number game.

# Import the random module so we can later use the randint function
import random

# Print to the user, request their name, and store it in the name variable
print('Hello what is your name?')
name = input()

# Print to the user
print('Well, ' + name + ', I''m thinking of a number between 1 and 20')

# Call the random module and use the randint function to choose a random number between 1 and 20 and set it to a
# variable
secretNumber = random.randint(1, 20)

# For loop for user guesses
for guessesTaken in range(1, 7):
    # Request the user to take a guess, take the input, change it to an integer for later comparison
    print('Take a guess')
    guess = int(input())

    # If statement to compare the user's guess to the secret number
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('You guess is too high.')
    else:
        # This condition is for the correct guess
        break

# Final if statement to confirm if the user got the guess correct or ran out of guesses via the else statement
if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope, the number I was thinking of was ' + str(secretNumber))