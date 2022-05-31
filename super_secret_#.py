from ast import Expression
import random


def guess(x):
    random_num  = random.randint(1,x)
    guess = 0
    while guess != random_num:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            if guess < random_num:
                print("Sorry. You guessed to low.")
            elif guess > random_num:
                print("Sorry. You guessed to high")
    print(f"Congrats! {guess} is correct!")

guess(100)