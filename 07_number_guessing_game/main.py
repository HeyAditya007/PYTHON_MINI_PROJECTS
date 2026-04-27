# THIS IS SIMPLE NUMBER GUESSING GAME BETWEEN RANGE(1,100)
import random

secret_number = random.randint(1, 100)
guess  = 0
attempts = 0

while guess != secret_number:
    guess = int(input("enter the a number:  "))
    attempts += 1


    if guess > secret_number:
        print("too high ")

    elif guess < secret_number:
        print("Too low ")
    else:
        print(f"you are correct your guess is {secret_number} actully is secret number.")
        print(f"it took you {attempts} to guess the right number")        