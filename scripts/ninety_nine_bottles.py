import sys
import time


PAUSE = 2


def main():
    print('Ninety-Nine Bottles Song!')
    print()
    print('Press Ctrl-C to exit ...')

    time.sleep(2)

    bottles = 99

    try:
        while bottles > 1:
            print(f'{bottles} of the milk on the wall,')
            time.sleep(PAUSE)
            print(f'{bottles} bottles of milk,')
            time.sleep(PAUSE)
            print(f'Take one round, pass it around,')
            time.sleep(PAUSE)
            bottles -= 1
            print(f'{bottles} bottles of the milk on the wall!')
            time.sleep(PAUSE)
            print()

        print('1 bottle of the milk on the wall,')
        time.sleep(PAUSE)
        print('1 bottle of the milk,')
        time.sleep(PAUSE)
        print('Take it down, pass it around,')
        time.sleep(PAUSE)
        print('No more bottles of milk on the wall!')

    except KeyboardInterrupt:
        print()
        print('Thanks for singing!')
        sys.exit()


if __name__ == '__main__':
    main()
