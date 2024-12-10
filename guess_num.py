import random

def guess_num():
    num = random.randint(1, 100)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < num:
                print("Too low!")
            elif guess > num:
                print("Too high!")
            else:
                print("You got it!")
                break
        except ValueError:
            print("Guess a num :) ")
            continue

guess_num()