# update to version 1
# most basic use of functions
# start game by running main()
# main() function includes play_game() - could be in a separate file
# play_game() function includes entire gameplay - could be in a separate file

import random

# main() controls game play
# starts game, plays game
# asks user if they want to play again
# quits game when user enters "no" (or not "yes")


def main():
    while True:
        play_game()
        play_again = input("\nDo you want to play again? Yes/No: ").capitalize()
        if play_again != "Yes":
            print("Thanks for playing!")
            break


# play_game() function contains all game play
def play_game():
    print("\nWelcome to Rock, Paper, Scissors!")

    # literally followed exercise guide instructions to enter letter and convert to corresponding word
    user_choice = input("Enter your choice: R, P or S: ").upper()
    if user_choice == "R":
        user_choice = "Rock"
    elif user_choice == "P":
        user_choice = "Paper"
    elif user_choice == "S":
        user_choice = "Scissors"
    print(f"You: {user_choice}")

    # literally followed exercise guide instructions to make
    # random choice of 0, 1 or 2 and translate to rock, paper or scissors
    choice = [0, 1, 2]
    computer_choice = random.choice(choice)

    if computer_choice == 0:
        computer_choice = "Rock"
    elif computer_choice == 1:
        computer_choice = "Paper"
    elif computer_choice == 2:
        computer_choice = "Scissors"
    print(f"Computer: {computer_choice}")

    # determines the winner (or draw)
    if user_choice == computer_choice:
        print("You chose the same, it's a draw!")
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print("Rock smashes Scissors. You win!")
        else:
            print("Paper wraps Rock. You lose!")
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print("Paper wraps Rock. You win!")
        else:
            print("Scissors cut Paper. You lose!")
    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            print("Scissors cut Paper. You win!")
        else:
            print("Rock smashes Scissors. You lose!")

# run main() function which will start the game
# functions above do nothing until main() is run
main()


# ////////////////// ALTERNATIVE UPDATED CODE ///////////////////////
#
# print("Welcome to Rock, Paper, Scissors!")
# player_choice = input("Enter your choice; rock, paper or scissors: ").lower()
#
# items = ['rock', 'paper', 'scissors']
# computer_choice = random.choice(items)
#
# if player_choice == computer_choice:
#     print(f"You both chose {player_choice}, you draw!")
# elif player_choice == "rock":
#     if computer_choice == "scissors":
#         print("Rock smashes Scissors, you win!")
#     else:
#         print("Paper wraps Rock, you lose!")
# elif player_choice == "paper":
#     if computer_choice == "rock":
#         print("Paper wraps Rock, you win!")
#     else:
#         print("Scissors cut Paper, you lose!")
# elif player_choice == "scissors":
#     if computer_choice == "paper":
#         print("Scissors cut Paper, you win!")
#     else:
#         print("Rock smashes Scissors, you lose!")
