# Guessing Game
import random

min_ = 1
max_ = 20
secret_number = random.randint(min_, max_)

for i in range(5):
    print("-"*50, f"Attempts {i+1}/5")

    usr_num = int(input(f"Guess the secret number (between {min_} and {max_}): "))

    if usr_num == secret_number:
        print("Congratulations! You've guessed the secret number.")
        break
    elif usr_num < secret_number:
        print("Too low! Try again.")
    elif usr_num > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Invalid input. Please enter a number between {min_} and {max_}.")