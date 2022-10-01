import sys
import time


def main():
    print('The Collatz Sequence experiment!')
    print('The Collatz Sequence is a sequence of numbers produced from a starting number n, following three rules: ')
    print('1. If n is even, the next number is n / 2.')
    print('2. If n is odd, the next number is 3n + 1.')
    print('3. If n is 1, stop. Otherwise, repeat.')
    print()

    print('Enter a starting number (greater than 0) or QUIT: ')
    response = input('> ').rstrip().upper()

    if not response.isdecimal() or int(response) <= 0:
        print('You must enter the integer greater than 0!')
        sys.exit()

    n = int(response)
    print(n, end='', flush=True)

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        print(', ' + str(n), end='', flush=True)
        time.sleep(0.3)

    print()


if __name__ == '__main__':
    main()
