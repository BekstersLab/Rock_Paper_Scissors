# use import random for use in get_computer_choice() function
import random

def welcome_message():
    name = input("Hello, please enter your name: ").capitalize()
    print(f"\nWelcome to Rock, Paper, Scissors {name}!")
    print("We are going to play seven games, may the best player win!")
    return name #return name so it can be used elsewhere in files

def get_player_choice():
    choice = input("\nChoose Rock, Paper or Scissors: ").capitalize() # use capitalize to convert user input
    return choice


def get_computer_choice():
    items = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(items)
    # print the computer choice as proof
    print(f"Computer: {computer_choice}")
    return computer_choice


# write scores to a file
def write_scores_to_file(name, player_score, computer_score):
    with open('game_scores.txt', 'a') as file:
        file.write(f"Final Score: {name} {player_score} - Computer {computer_score}\n")