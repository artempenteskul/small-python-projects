import sys


NUMBER_OF_ATTEMPTS = 10


def main():
    print('The Hangman Game!')
    print('It\'s a game for two players.')
    print('The goal of the game is to guess word, which another player thought of.')
    print('You can guess it by a letters (like in usual hangman game), and you\'l also have the category of word.')
    print('By default, you have 10 attempts to guess the word.')
    print()

    player_1 = get_player_name(1)
    player_2 = get_player_name(2)
    print()

    score = {player_1: 0, player_2: 0}

    number_of_rounds = get_rounds_number()
    number_of_games = number_of_rounds * 2

    print()
    print(f'MATCH: {player_1} vs {player_2}')
    print()

    move_guess_turn = player_1
    move_think_turn = player_2

    for game in range(number_of_games):
        print(f'GAME: {game + 1}')
        print(f'{move_think_turn} - your turn to think of a word!')
        print(f'{move_guess_turn} - your turn to guess the word!')

        print()
        print(f'{move_guess_turn} should close eyes.')
        print(f'{move_think_turn} will be asked to enter the word and its category.')

        print()
        input('Press enter to continue ...')
        print()

        category = get_word_category()
        word = get_word(category)


def get_player_name(player_number):
    print(f'Player {player_number}, enter your name: ')
    name = input('> ')
    return name


def get_rounds_number():
    print('At first, we need to decide how many you want to play: (Q to quit)')

    while True:
        response = input('> ')
        if response.isdecimal() and int(response) > 0:
            return int(response)

        print('You need to enter how many rounds do you wanna play: (Q to quit)')


def get_word_category():
    print('Enter the category for the word: ')
    category = input('> ')
    while True:
        response = input(f'Your category is {category}, is it right? Y/N: ')
        if response.lower().startswith('y'):
            return category
        elif response.lower().startswith('n'):
            print('Enter correct category: ')
            category = input('> ')
        else:
            continue


def get_word(category):
    print(f'Enter the word for, your category for this round is {category}: ')
    word = input('> ')
    while True:
        response = input(f'Your word for category {category} is {word}, is it right? Y/N: ')
        if response.lower().startswith('y'):
            return word
        elif response.lower().startswith('n'):
            print('Enter correct word: ')
            word = input('> ')
        else:
            continue


def clear_screen():
    print('\n' * 100)


if __name__ == '__main__':
    main()
