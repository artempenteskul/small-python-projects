import random


NUM_DIGITS = 3
NUM_GUESSES = 10


def get_secret_num():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7' '8', '9']
    random.shuffle(numbers)

    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += numbers[i]

    return secret_num


def get_clues(guess, secret_num):
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'

    random.shuffle(clues)
    return ' '.join(clues)


def main():
    print('Bagels, a deductive logic game!')
    print(f'I\'m thinking of {NUM_DIGITS}-number with no repeated digits. Try to guess the number!')
    print('Here are some rules: ')
    print('  Pico => one digit is correct but in the wrong position')
    print('  Fermi => one digit is correct and in the right position')
    print('  Bagels => no digits is correct')

    while True:
        secret_num = get_secret_num()
        print('I have thought a number. You have {NUM_GUESSES} tries to guess it.')

        num_guesses = 1
        while num_guesses <= NUM_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{num_guesses}: ')
                guess = input('> ')

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > NUM_GUESSES:
                print('You are run out of guesses!')
                print(f'The answer was {secret_num}')

        print('Do you wanna play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing!')


if __name__ == '__main__':
    main()
