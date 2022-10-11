import sys
import random


def main():
    print('The Guess The Number Game!')
    print()
    print('I am thinking of a number between 1 and 100 ...')

    secret_num = random.randint(1, 100)
    number_of_guesses = get_number_of_guesses()

    for i in range(number_of_guesses):
        print(f'You have {number_of_guesses - i} guesses left. Take a guess!')
        guess = ask_for_guess()
        if guess == secret_num:
            print(f'Yay! You guessed the number! It was {secret_num}!')
            sys.exit()

        if guess < secret_num:
            print('Your guess is too low!')
        else:
            print('Your guess is too high!')

    print(f'Game over! You lost! The number was {secret_num}!')


def ask_for_guess():
    while True:
        guess = input('> ')

        if guess.isdecimal() and 100 >= int(guess) >= 1:
            return int(guess)

        print('Please, enter the number between 1 and 100!')


def get_number_of_guesses():
    response = ''
    while response not in range(1, 10):
        print('How many guesses do you wanna have? (from 1 to 10): ')
        response = input('> ')
        if not response.isdecimal():
            continue

        response = int(response)

    return response


if __name__ == '__main__':
    main()
