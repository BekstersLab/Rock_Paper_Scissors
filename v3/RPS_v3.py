# version 3 - change gameplay so it is best of 7 games.
# remove while True
# use for loop to specify range eg. 7

import random

# declare variables for counting score, set to 0 at start of play
player_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors!")
print("We are going to play seven games, may the best player win!")

# main game loop
# use a for loop to specify number of games played
for _ in range(7):
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

# determine the winner after 7 games
if player_score == computer_score:
    print("It's a draw!")
elif player_score > computer_score:
    print(f"Congratulations, you win with a final score of {player_score}:{computer_score}")
elif computer_score > player_score:
    print(f"Commiserations, the computer wins with a final score of {computer_score}:{player_score}")

# write scores to a file
with open('game_scores_v3.txt', 'a') as file:
    file.write(f"Final Score: You - {player_score}, Computer - {computer_score}\n")