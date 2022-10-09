import sys
import math


def main():
    print('The Factor Finder Program!')
    print('This program finds all the factors of the number.')
    print('If a number only has two factors (1 and itself), we call that a prime number. Otherwise, we call it a composite number.')

    while True:
        print('Enter a positive whole number to factor (or QUIT): ')
        response = input('> ')

        if response.lower().startswith('q'):
            sys.exit()

        if not (response.isdecimal() and int(response) > 0):
            continue

        number = int(response)

        factors = []

        for i in range(1, int(math.sqrt(number)) + 1):
            if number % i == 0:
                factors.append(i)
                factors.append(number // i)

        factors = list(set(factors))
        factors.sort()

        print('--- Results --- ')
        for factor in factors:
            if factor == factors[-1]:
                print(f'{factor}.')
            else:
                print(f'{factor}, ', end='')

        if len(factors) == 2:
            print('This number is prime!')
        else:
            print('This number is composite!')


if __name__ == '__main__':
    main()
