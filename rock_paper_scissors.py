
import random


def rock_paper_scissors():
    """rock paper scissor game played against the ghost"""
    choices = {
    "1": ("Rock"),
    "2": ("Paper"),
    "3": ("Scissors"),
    }
    # Users choice
    user_choice = input("\nEnter your choice (1-Rock, 2-Paper, 3-Scissors): ")
    # Choice validation
    if user_choice not in choices.keys():
        print("Invalid. Please enter your number of choice.")
        return rock_paper_scissors()

    # Ghosts choice
    ghost_choice = random.choice(list(choices.keys()))
    # Determine the winner
    if user_choice == ghost_choice:
        print(f"\nYou chose: {user_choice}.")
        print(f"The Old Ghost Lady: {ghost_choice}")
        print("\nIt's a tie! Let's go again.")
        return rock_paper_scissors()
    elif (user_choice == "1" and ghost_choice == "3") or (user_choice == "2" and ghost_choice == "1") or (user_choice == "3" and ghost_choice == "2"):
        print(f"\nYou chose: {user_choice}.")
        print(f"The Old Ghost Lady: {ghost_choice}")
        print(f"\nYou win!")
        return True
    else:
        print(f"\nYou chose: {user_choice}.")
        print(f"The Old Ghost Lady: {ghost_choice}")
        print(f"\nYou lose!")
        return False