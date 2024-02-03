import random

def get_user_choice():
    user_action = input("Enter a choice (rock, paper, scissors): ")
    return user_action.lower()

def get_computer_choice():
    possible_actions = ["rock", "paper", "scissors"]
    return random.choice(possible_actions)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins."
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins."
    elif user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins."
    else:
        return "Invalid input. Please choose rock, paper, or scissors."

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")
        print(determine_winner(user_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
