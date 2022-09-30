import sys
import random


def main():
    print('The carrot in the box game!')
    print('This is a bluffing game for two human players. Each player has a box.')
    print('One box has a carrot inside. To win, you must have the box with carrot.')
    print()
    print('This is a very simple and silly game!')
    print('')

    input('Press Enter to begin ...')
    print()

    player_one = input('Human Player 1, enter your name: ').rstrip()
    player_two = input('Human Player 2, enter your name: ').rstrip()

    score = {
        player_one: 0,
        player_two: 0
    }

    print()
    match = f'MATCH: {player_one} vs {player_two}'
    print(match)

    move_bluff_turn = 1
    move_guess_turn = 2

    games_counter = 1

    while True:
        print(f'SCORE: {player_one}({score[player_one]}) - {player_two}({score[player_two]})')
        print()
        print(f'GAME #{games_counter}')
        print()

        is_box_with_carrot = is_carrot_inside()
        player_to_bluff, player_to_guess = manage_players_roles(move_bluff_turn, move_guess_turn, player_one, player_two)

        print(f'Player {player_to_guess} should close eyes!')
        input(f'Player {player_to_bluff}, press enter to discover if carrot is inside your box ... ')
        print()

        if is_box_with_carrot:
            print('CARROT IS INSIDE YOUR BOX!')
        else:
            print('YOUR BOX IS EMPTY!')

        print('YOU NEED TO DECEIVE YOUR OPPONENT!')

        print()
        input('Press Enter to clear the screen ...')
        clear_console()

        guess_if_carrot_inside(is_box_with_carrot, score, player_to_guess, player_to_bluff)

        clear_console()
        move_bluff_turn, move_guess_turn = change_moves_turns(move_bluff_turn, move_guess_turn)
        games_counter += 1

        resume_game(score, player_one, player_two)


def clear_console():
    print('\n' * 300)


def is_carrot_inside():
    return random.choice((False, True))


def manage_players_roles(move_bluff_turn, move_guess_turn, player_one, player_two):
    if move_bluff_turn == 1 and move_guess_turn == 2:
        return player_one, player_two
    elif move_bluff_turn == 2 and move_guess_turn == 1:
        return player_two, player_two
    else:
        raise Exception


def guess_if_carrot_inside(is_box_with_carrot, score, player_to_guess, player_to_bluff):
    print('YOU NEED TO GUESS IS CARROT INSIDE BOX OR NOT!')
    response = input('Type Y if yes, or N if no: ').upper()
    if response.startswith('Y') and is_box_with_carrot is True:
        print('YOU ARE RIGHT! You earn 1 point!')
        score[player_to_guess] += 1
    elif response.startswith('N') and is_box_with_carrot is False:
        print('YOU ARE RIGHT! You earn 1 point!')
        score[player_to_guess] += 1
    else:
        print('YOU ARE WRONG! Your opponent earns 1 point!')
        score[player_to_bluff] += 1


def change_moves_turns(move_bluff_turn, move_guess_turn):
    if move_bluff_turn == 1 and move_guess_turn == 2:
        return 2, 1
    elif move_bluff_turn == 2 and move_guess_turn == 1:
        return 1, 2


def resume_game(score, player_one, player_two):
    response = input('DO YOU WANNA KEEP PLAYING? (q to QUIT)').rstrip().lower()
    if response.startswith('q'):
        print()
        print('--- FINAL SCORE ---')
        print(f'PLAYER {player_one}: {score[player_one]}')
        print(f'PLAYER {player_two}: {score[player_two]}')
        sys.exit()


if __name__ == '__main__':
    main()
