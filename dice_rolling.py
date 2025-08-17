import random

while True:
    a=input("do you want to roll the dice?(y/n): ").lower()
    if a == "y":
        print(random.randint(1,6))
    elif a == "n":
        print("thank you for playing!")
        break
    else:
        print("invalid input")

