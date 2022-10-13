import sys


NUMBER_OF_ATTEMPTS = 10


def main():
    print('The Hangman Game!')
    print('It\'s a game for two players.')
    print('The goal of the game is to guess word, which another player thought of.')
    print('You can guess it by a letters (like in usual hangman game), and you\'l also have the category of word.')
    print('By default, you have 10 attempts to guess the word.')
    print()

    number_of_rounds = get_rounds_number()
    number_of_games = number_of_rounds * 2


def get_rounds_number():
    print('At first, we need to decide how many you want to play: (Q to quit)')

    while True:
        response = input('> ')
        if response.isdecimal() and int(response) > 0:
            return int(response)

        print('You need to enter how many rounds do you wanna play: (Q to quit)')


def clear_screen():
    print('\n' * 100)


if __name__ == '__main__':
    main()
