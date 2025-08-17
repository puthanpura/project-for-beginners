import random
# Number Guessing Game
a=random.randint(1,100)
while True:
    guess=int(input("guess a number between 1 and 100: "))
    if guess>a:
        print("your guess is too high")
    elif guess<a:
        print("your guess is too low")
    else:
        print("you guessed it right")
        break