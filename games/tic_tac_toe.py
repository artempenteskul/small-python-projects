import random


X, O, BLANK = 'X', 'O', ' '
ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def main():
    print('Welcome to Tic-Tac-Toe Game')

    game_board = get_blank_board()
    possible_moves = [X, O]
    random.shuffle(possible_moves)
    move_player, wait_player = possible_moves

    while True:
        print(get_board_str(game_board))

        move = None
        while not is_valid_space(game_board, move):
            print(f'What\'s is {move_player}\'s move? (1-9)')
            move = input('> ')

        update_board(game_board, move, move_player)

        if is_winner(game_board, move_player):
            print(get_board_str(game_board))
            print(f'{move_player} has won the game!')
            break
        elif is_board_full(game_board):
            print(get_board_str(game_board))
            print('The game is a tie!')
            break

        move_player, wait_player = wait_player, move_player

    print()
    print('Thanks for playing!')


def get_blank_board():
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK
    return board


def get_board_str(board):
    return f'''
    {board['1']} | {board['2']} | {board['3']}   1  2  3
    --+---+--
    {board['4']} | {board['5']} | {board['6']}   4  5  6
    --+---+-- 
    {board['7']} | {board['8']} | {board['9']}   7  8  9
    '''


def is_valid_space(board, space):
    if board.get(space) == BLANK and space in ALL_SPACES:
        return True
    return False


def is_winner(board, player):
    if ((board['1'] == board['2'] == board['3'] == player) or
        (board['4'] == board['5'] == board['6'] == player) or
        (board['7'] == board['8'] == board['9'] == player) or
        (board['1'] == board['4'] == board['7'] == player) or
        (board['2'] == board['5'] == board['8'] == player) or
        (board['3'] == board['6'] == board['9'] == player) or
        (board['1'] == board['5'] == board['9'] == player) or
        (board['3'] == board['5'] == board['7'] == player)):
        return True
    return False


def is_board_full(board):
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True


def update_board(board, move, mark):
    board[move] = mark


if __name__ == '__main__':
    main()
