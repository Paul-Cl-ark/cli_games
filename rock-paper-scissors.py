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


def play():
    computer_move = choice(moves)
    player_move = input('\nEnter \'rock\', \'paper\' or \'scissors\'... ')
    print(computer_move, player_move)


play()
