import sys
import time


REWARD = 5
NUMBER_OF_ATTEMPTS = 10


def main():
    print('The Hangman Game!')
    print('It\'s a game for two players.')
    print('The goal of the game is to guess word, which another player thought of.')
    print('You can guess it by a letters (like in usual hangman game), and you\'l also have the category of word.')
    print('By default, you have 10 attempts to guess the word.')
    print()

    player_1, player_2 = get_players_names()
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
        print()
        print(f'{move_guess_turn} - your turn to guess the word!')
        print(f'{move_think_turn} - your turn to think of a word!')

        print()
        print(f'{move_guess_turn} should close eyes!')
        print(f'{move_think_turn} will be asked to enter the word and its category.')

        print()
        input('Press enter to continue ...')
        print()

        category = get_word_category()
        word = get_word(category)

        print()
        input('Press Enter to clear the screen ...')
        clear_screen()

        print(f'It\'s time for {move_guess_turn} to guess the word.')
        print()

        guess_the_word(word, category, move_guess_turn, move_think_turn, score)

        print()
        input('Press Enter to begin next game ...')
        clear_screen()

        move_guess_turn, move_think_turn = move_think_turn, move_guess_turn


def get_players_names():
    print('Human Player 1, enter your name: ')
    player_1 = input('> ').upper()
    print('Human Player 2, enter your name: ')
    player_2 = input('> ').upper()

    while player_1 == player_2:
        print(f'Name {player_1} is already taken. Choose another: ')
        player_2 = input('> ').upper()

    return player_1, player_2


def get_rounds_number():
    print('At first, we need to decide how many rounds you want to play: (Q to quit)')

    while True:
        response = input('> ')
        if response.isdecimal() and int(response) > 0:
            return int(response)

        print('You need to enter how many rounds do you wanna play: (Q to quit)')


def get_word_category():
    print('Enter the category for the word: ')
    category = input('> ').upper()
    while True:
        print(f'Your category is {category}, is it right? Y/N: ')
        response = input('> ')
        if response.lower().startswith('y'):
            return category
        elif response.lower().startswith('n'):
            print('Enter correct category: ')
            category = input('> ').upper()
        else:
            continue


def get_word(category):
    print(f'Enter the word, your category for this round is {category}: ')
    word = input('> ').upper()
    while True:
        print(f'Your word for category {category} is {word}, is it right? Y/N: ')
        response = input('> ')
        if response.lower().startswith('y'):
            return word
        elif response.lower().startswith('n'):
            print('Enter correct word: ')
            word = input('> ').upper()
        else:
            continue


def guess_the_word(word, category, move_guess_turn, move_think_turn, score):

    guessed_letters = []
    word_guess_progress = check_the_word(word, guessed_letters)

    print(f'The category of the word is {category}.')
    print(f'Your current progress: {word_guess_progress}')
    print()

    for i in range(NUMBER_OF_ATTEMPTS):
        print(f'GUESS #{i+1}')
        print()

        guess, is_full_word = get_guess()

        if is_full_word:
            print(f'Your guess of full word: {guess}.')
            print('Comparing to the actual word ...')
            print()
            time.sleep(2)

            if word == guess:
                print(f'You are right! You earn {REWARD} points! The word was: {word}.')
                score[move_guess_turn] += REWARD
                return
            else:
                print(f'You lose this game! Your opponent earns {REWARD} points! The word was: {word}.')
                score[move_think_turn] += REWARD
                return

        else:
            guessed_letters.append(guess)
            word_guess_progress = check_the_word(word, guessed_letters)
            print('Looking for your letter in word ...')
            time.sleep(2)
            print()

            print(f'Current word guess progress: {word_guess_progress}')
            print()

            if word_guess_progress.replace(' ', '') == word:
                print(f'Seems that you have already won! You earn {REWARD} points! The word was: {word}.')
                score[move_guess_turn] += REWARD
                return

            input('Press Enter to take another guess ...')
            print()

    print(f'You lose this game! Your opponent earns {REWARD} points! The word was: {word}.')
    score[move_think_turn] += REWARD
    return


def get_guess():
    print('Are you ready to guess full word? Y/N: ')
    response = input('> ')
    while True:
        if response.lower().startswith('y'):
            print('Your guess of full word: ')
            word = input('> ').upper()
            return word, True
        elif response.lower().startswith('n'):
            print('Your letter: ')
            letter = input('> ').upper()
            while len(letter) != 1:
                print('You entered more than one letter, you need to enter only one: ')
                letter = input('> ').upper()
            return letter, False
        else:
            print('Are you ready to guess full word? Y/N: ')
            response = input('> ')


def check_the_word(word, guessed_letters):
    if len(guessed_letters) == 0:
        return '_ ' * len(word)

    word_progress = []
    word_letters = list(word)

    for letter in word_letters:
        if letter in guessed_letters:
            word_progress.append(letter)
        else:
            word_progress.append('_')

    return ' '.join(word_progress)


def clear_screen():
    print('\n' * 100)


if __name__ == '__main__':
    main()
