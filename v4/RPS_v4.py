# update best of 7 games code to incorporate functions in separate game_functions.py file
# still need to define additional functions to reduce code further

from game_functions import welcome_message, get_player_choice, get_computer_choice, write_scores_to_file

# declare variables for counting score, set to 0 at start of play
player_score = 0
computer_score = 0

# welcome_message function returns the players name
name = welcome_message()

# main game loop
# use a for loop to specify number of games played
for _ in range(7):
    # use get_player_choice function to ask for player input. Returns choice and assigns to player_choice variable
    player_choice = get_player_choice()
    # use get_computer_choice function pick a random choice for the computer.
    # returns choice and assigns to computer_choice variable
    computer_choice = get_computer_choice()

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
    print(f"Score: {name} - {player_score}, Computer - {computer_score}")

# determine the winner after 7 games
if player_score == computer_score:
    print("It's a draw!")
elif player_score > computer_score:
    print(f"Congratulations, you win with a final score of {player_score}:{computer_score}")
elif computer_score > player_score:
    print(f"Commiserations, the computer wins with a final score of {computer_score}:{player_score}")

# use function from game_functions.py file
write_scores_to_file(name, player_score, computer_score)

