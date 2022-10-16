import time
import random


def main():
    print('The Million Dice Stats Simulation!')
    print()

    print('Enter how many six-sided dices you want to roll: ')
    number_of_dices = int(input('> '))

    RESULTS = {}

    for i in range(number_of_dices, (number_of_dices * 6) + 1):
        RESULTS[i] = 0

    print()
    print(f'Simulating 1_000_000 rolls of the {number_of_dices} dices ...')

    last_print_time = time.time()

    for i in range(1_000_000):
        if time.time() > last_print_time + 1:
            print(f'{round(i / 10_000, 1)}% done ...')
            last_print_time = time.time()

        total = 0
        for j in range(number_of_dices):
            total += random.randint(1, 6)

        RESULTS[total] += 1

    print()
    print('TOTAL - ROLLS - PERCENTAGE')
    for i in range(number_of_dices, (number_of_dices * 6) + 1):
        rolls = RESULTS[i]
        percentage = round(rolls / 10_000, 2)
        print(f'{i} - {rolls} rolls - {percentage}%')


if __name__ == '__main__':
    main()
