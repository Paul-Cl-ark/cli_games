from random import choice

# get computer input
# prompt user to enter move
# validate move
# move not valid -> you lose
# else calculate winner
# draw, win, or loss
# keep tally of score
# best to 5 wins


moves = ('rock', 'paper', 'scissors')


def print_winner(winner):
    print('\n')
    if winner == 'draw':
        print('DRAW...')
    elif winner == 'computer':
        print('YOU LOSE!')
    else:
        print('YOU WIN!')
    print('\n--------------------------------------')


def calculate_winner(computer_move, player_move):
    if computer_move == player_move:
        return 'draw'
    elif computer_move == 'rock' and player_move == 'scissors' \
            or computer_move == 'scissors' and player_move == 'paper' \
            or computer_move == 'paper' and player_move == 'rock':
        return 'computer'
    else:
        return 'player'


def get_symbol(input):
    symbol_dictionary = {
        'rock': '👊',
        'paper': '✋',
        'scissors': '✌️'
    }
    return symbol_dictionary[input]


def print_moves(computer_move, player_move):
    print('\n', get_symbol(computer_move), '🆚',
          get_symbol(player_move), sep="   ")


def play():

    computer_move = choice(moves)
    player_move = input('\nEnter \'rock\', \'paper\' or \'scissors\'... ')

    print_moves(computer_move, player_move)
    winner = calculate_winner(computer_move, player_move)

    print_winner(winner)
    return winner


scores = {
    'computer': 0,
    'player': 0,
    'draw': 0
}

while scores['computer'] < 3 and scores['player'] < 3:
    winner = play()
    scores[winner] += 1

    print('\n')
    print('COMPUTER:', scores['computer'])
    print('YOU:', scores['player'])
    print('DRAW:', scores['draw'])
    print('\n--------------------------------------')
else:
    print('\n')
    if winner == 'computer':
        print('YOU LOSE!')
    else:
        ('YOU WIN!')
