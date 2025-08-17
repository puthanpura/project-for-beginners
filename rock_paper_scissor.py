import random
choices=("r","s","p")

while True:
    your_choice=input("Enter your choice (r for rock, s for scissors, p for paper): ").lower()
    computer_choice=random.choice(choices)
    if your_choice not in choices:
        print("Invalid choice. Please enter 'r', 's', or 'p'.")
    elif your_choice == computer_choice:
            print(f"Both chose {your_choice}. It's a tie!")
    elif ((your_choice == "r" and computer_choice == "s") or \
        (your_choice == "s" and computer_choice == "p") or \
        (your_choice == "p" and computer_choice == "r")):
        print(f"You chose {your_choice} and the computer chose {computer_choice}. You win!")
    else:
        print(f"You chose {your_choice} and the computer chose {computer_choice}. You lose!")
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'n':
        print("Thanks for playing!")
        break