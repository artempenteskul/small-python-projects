import random


def main():
    print('The Powerball Lottery!')
    print('Each powerball lottery ticket costs $2. The jackpot for this game is $1.56 billion dollars!')
    print('It doesn\'t matter what the jackpot is, though, because the odds are in 1 to 2292,201,338!')
    print('So you won\'t win!')
    print()
    print('This simulation gives you the thrill of playing without wasting money.')
    print()

    while True:
        print('Enter 5 different numbers from 1 to 69, with space between each number (e.g. 5, 19, 22, 43, 12): ')
        response = input('> ')
        numbers = response.split()

        if len(numbers) != 5:
            print('Please enter 5 numbers, separated by spaces.')
            continue

        if not all(num.isdecimal() for num in numbers):
            print('Please enter numbers, like 27, 35, or 62.')
            continue

        if not all(1 <= int(num) <= 69 for num in numbers):
            print('Please enter numbers between 1 and 69.')
            continue

        if len(set(numbers)) != 5:
            print('You must enter 5 different numbers.')
            continue

        break

    while True:
        print('Enter the powerball number from 1 to 26 (e.g. 13): ')
        response = input('> ')

        try:
            powerball = int(response)
        except ValueError:
            print('Please enter a number, like 3, 15, or 22.')
            continue

        if not 1 <= powerball <= 26:
            print('The powerball number must be between 1 and 26.')
            continue

        break

    while True:
        print('How many times do you want to play? (max 1_000_000): ')
        response = input('> ')

        try:
            play_num = int(response)
        except ValueError:
            print('Please enter a number, like 3, 15, or 22000.')
            continue

        if not 1 <= play_num <= 1_000_000:
            print('You can play between 1 and 1_000_000 times.')
            continue

        break


if __name__ == '__main__':
    main()

