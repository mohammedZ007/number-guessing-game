#Python Game

import random

number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 10.")
print("You have 3 chances to guess it.\n")

for chance in range(1, 4):
    try:
        guess = int(input(f"Chance {chance}/3 - Enter your guess: "))

        if guess < 1 or guess > 10:
            print("Invalid input! Please choose a number between 1 and 10.")
            continue

        if guess == number:
            print("Congratulations! You guessed the correct number. You WIN!")
            break

        difference = abs(number - guess)

        if difference <= 2:
            print("You are near to the correct number.")
        else:
            print("You are far away from the correct number.")

    except ValueError:
        print("Invalid input! Please enter a number between 1 and 10.")

else:
    print(f"Game Over! The correct number was {number}.")
