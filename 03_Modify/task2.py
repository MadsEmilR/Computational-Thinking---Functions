'''
Adapt the code to create a guessing game. Your game should ask the user for a username and greet him/her personally. 
Additionally, it should report a score (the number of guesses needed to guess the number correctly) at the end of the round. 
When the round is finished, your game should ask the user if he/she wants to play again.
'''

import random

randomNumber = random.randint(1, 50)
guess = int(
    input("I selected a secret number between 1 and 50. Try to guess it:\n>"))

while guess != randomNumber:
    if guess < randomNumber:
        guess = int(input("Wrong - your number is to small! Guess again.\n>"))
    elif guess > randomNumber:
        guess = int(input("Wrong - your number is to big! Guess again.\n>"))

print(f"Good job! You guessed {randomNumber} correctly")
