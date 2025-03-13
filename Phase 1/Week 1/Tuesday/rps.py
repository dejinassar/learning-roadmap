import sys
import random

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        return "You win!"
    else:
        return "💻 Computer wins!"

while True:
    print("\n=== Rock, Paper, Scissors Game ===\n")
    
    player_input = input("Enter: \n1 for Rock \n2 for Paper \n3 for Scissors ✂️\n\nYour choice: ")
    
    try:
        player_choice = int(player_input)
        if player_choice not in choices:
            raise ValueError
    except ValueError:
        print("Invalid input! Please enter 1, 2, or 3.")
        continue

    computer_choice = get_computer_choice()

    print(f"\nYou picked: {choices[player_choice]}")
    print(f"Computer picked: {choices[computer_choice]}\n")

    result = determine_winner(player_choice, computer_choice)
    print(result)

    play_again = input("\nWant to play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("\nThanks for playing!")
        break
