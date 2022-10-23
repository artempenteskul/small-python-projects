X, O, BLANK = 'X', 'O', ' '
ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def main():
    print('Welcome to Tic-Tac-Toe Game')

    game_board = get_blank_board()
    player_1, player_2 = X, O

    while True:
        print(get_board_str(game_board))

        move = None
        while not is_valid_space(game_board, move):
            print(f'What\'s is {player_1}\'s move? (1-9)')
            move = input('> ')

        update_board(game_board, move, player_1)

        if is_winner(game_board, player_1):
            print(get_board_str(game_board))
            print(f'{player_2} has won the game!')
            break
        elif is_board_full(game_board):
            print(get_board_str(game_board))
            print('The game is a tie!')
            break

        player_1, player_2 = player_2, player_1
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
    {board['9']} | {board['8']} | {board['9']}   7  8  9
    '''


def is_valid_space(board, space):
    return True if board[space] == BLANK and space in ALL_SPACES else False


if __name__ == '__main__':
    main()
