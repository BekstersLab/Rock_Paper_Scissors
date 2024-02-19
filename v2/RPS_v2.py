# version 2 - rewrite. No functions
# while loop for game play, while True execute code
# play again? breaks if user doesn't enter "yes"
# keeps playing if enter yes and appends score to a file

import random

# declare variables for counting score, set to 0 at start of play
player_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors!")

# main game loop
while True:
    # get the players choice
    player_choice = input("\nChoose Rock, Paper or Scissors: ").capitalize()
    print(f"You: {player_choice}")

    # randomly choose for computer
    items = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(items)
    print(f"Computer: {computer_choice}")

    # if statement determines the winner and updates score
    if player_choice == computer_choice:
        print(f"You both chose {player_choice}, you draw!")
    elif player_choice == "Rock":
        if computer_choice == "Scissors":
            print("Rock smashes Scissors, you win!")
            player_score += 1
        else:
            print("Paper wraps Rock, you lose!")
            computer_score += 1
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            print("Paper wraps Rock, you win!")
            player_score += 1
        else:
            print("Scissors cut Paper, you lose!")
            computer_score += 1
    elif player_choice == "Scissors":
        if computer_choice == "Paper":
            print("Scissors cut Paper, you win!")
            player_score += 1
        else:
            print("Rock smashes Scissors, you lose!")
            computer_score += 1

    # display current score after each play
    print(f"Score: You - {player_score}, Computer - {computer_score}")

    # ask player if they want to play again
    play_again = input("\nDo you want to play again? Yes/No: ").capitalize()
    if play_again != "Yes":
        break # exit the loop if player doesn't want to play again

if player_score == computer_score:
    print("It's a draw!")
elif player_score > computer_score:
    print(f"Congratulations, you win with a final score of {player_score}:{computer_score}")
elif computer_score > player_score:
    print(f"Commiserations, the computer wins with a final score of {computer_score}:{player_score}")

# write scores to a file
with open('game_scores_v2.txt', 'a') as file:
    file.write(f"Final Score: You - {player_score}, Computer - {computer_score}\n")