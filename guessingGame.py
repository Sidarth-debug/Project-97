import random

random_number = random.randint(1,9)
chances = 0

while chances<5:
    guessed_number = int(input("Guess the number "))
    if guessed_number<random_number:
        print("You have to guess higher.")
    elif guessed_number>random_number:
        print("You have to guess lower.")
    else :
        print("Congratulations. You guessed correctly.")
    chances = chances+1 
if chances==5:
    print("You lost.")   