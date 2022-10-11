import sys
import random


def main():
    print('The Guess The Number Game!')
    print()
    print('I am thinking of a number between 1 and 100 ...')

    secret_num = random.randint(1, 100)

    for i in range(10):
        print(f'You have {10 - i} guesses left. Take a guess!')
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


if __name__ == '__main__':
    main()
