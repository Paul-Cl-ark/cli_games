from random import randrange
board = [['-' for number in range(1, 4)] for row in range(1, 4)]


def display_board(board):
    print('\n')
    for row in board:
        print(' +-----------+\n', *row, sep=' | ', end=" |\n")
    else:
        print(' +-----------+\n')


def add_move_to_board(board, position, sign):
    board[position[0]][position[1]] = sign
    return board


def enter_move(board):
    move = input('Enter a space between 1 and 9: ')
    move_tuple = get_field(move)
    if not move_tuple:
        enter_move(board)

    free_fields = make_list_of_free_fields(board)
    if not move_tuple in free_fields:
        return enter_move(board)
    else:
        return add_move_to_board(board, move_tuple, 'x')


def make_list_of_free_fields(board):
    free_fields = []
    for row_index, row in enumerate(board):
        for field_index, field in enumerate(row):
            if field == '-':
                free_fields.append((row_index, field_index))
    return free_fields


def get_field(key):
    key_map = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2)
    }

    if not key in key_map:
        return None
    return key_map[key]


def victory_for(board, sign):
    for row_index, row in enumerate(board):
        if all(item == sign for item in row):
            return True
        elif all(board[item][row_index] == sign for item in range(0, 3)):
            return True
        else:
            return False


def draw_move(board):
    move = (randrange(9))
    move_tuple = get_field(str(move))
    free_fields = make_list_of_free_fields(board)
    if (not move_tuple in free_fields):
        return draw_move(board)
    else:
        return add_move_to_board(board, move_tuple, 'o')


def play(board):
    while not victory_for(board, 'x') and not victory_for(board, 'o'):
        display_board(board)
        new_board = enter_move(board)

        if victory_for(new_board, 'x'):
            display_board(new_board)
            print('\nx wins!')
            return print('\nGame over!')
        new_board_2 = draw_move(new_board)
        if victory_for(new_board_2, 'o'):
            display_board(new_board_2)
            print('\no wins!')
            return print('\nGame over!')
        play(new_board_2)


play(board)
