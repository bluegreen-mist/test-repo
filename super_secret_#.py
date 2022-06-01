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


def comp_guess(x):
    play = input(f"Please think of a number between 1 and {x}. Once you have done so please type yes ->")
    guess = "no"
    max_num = x
    min_num = 1
    comp_guess = round((max_num + min_num) / 2)
    
    first_time = 1
    if play == "yes":
        while guess != "yes":
            
            guess = input(f"Is your number {comp_guess} | higher | lower | yes | ->").lower
            if guess == "higher":
                min_num = comp_guess
                comp_guess = round((max_num + min_num) / 2)
                
            elif guess == "lower":
                max_num = comp_guess
                comp_guess = round((max_num + min_num) / 2)
                
    
        

        print("Whoooo I did it! That was so much fun! ")

comp_guess(999)

