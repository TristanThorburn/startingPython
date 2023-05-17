# code along to: https://youtu.be/eWRfhZUzrAc

import random

def get_choices():
    player_choice = input('Enter a choice (rock, paper, scissors): ')
    options = ['paper', 'rock', 'scissors']
    computer_choice = random.choice(options)

    choices = {'player':player_choice, 'computer': computer_choice}

    return choices

def check_win(player, computer):
    # print('You chose ' + player + ', Computer chose ' + computer)
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a TIE!"
    
    # elif player == 'rock' and computer == 'scissors':
    #     return "rock smashes scissors, you WIN!"
    # elif player == 'rock' and computer == 'paper':
    #     return 'paper covers rock, you LOSE :('

    elif player == 'rock':
        if computer == 'scissors':
            return 'rock smashes scissors, you WIN!'
        else:
            return 'paper covers rock, you LOSE :('
        
    elif player == 'paper':
        if computer == 'rock':
            return 'paper covers rock, you WIN!'
        else:
            return 'scissors cut paper, you LOSE :('
        
    elif player == 'scissors':
        if computer == 'paper':
            return 'paper covers rock, you WIN!'
        else:
            return 'rock smashes scissors, you LOSE :('

game_choices = get_choices()

result = check_win(game_choices['player'], game_choices['computer'])

print(result)