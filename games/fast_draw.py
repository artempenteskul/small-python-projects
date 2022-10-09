import sys
import time
import random


def main():
    print('The Fast Draw Game!')
    print()
    print('Time to test your reflexes and see if you are the fastest draw in the west!')
    print('When you see "DRAW!", you have 0.3 seconds to to press Enter.')
    print('But you lose if you press Enter before "DRAW!" appears.')
    print()
    input('Press Enter to begin ...')

    while True:
        print()
        print('It\'s a high noon ...')
        time.sleep(random.randint(2, 6))
        print('DRAW!')
        draw_time = time.time()
        input()
        time_res = time.time() - draw_time

        if time_res < 0.01:
            print('You drew before the input! You lose!')
        elif time_res > 0.3:
            time_res = round(time_res, 4)
            print(f'You took {time_res} seconds to draw, too slow! You lose!')
        else:
            time_res = round(time_res, 4)
            print(f'You took {time_res} seconds to draw!')
            print('You are the fastest draw in the west! You win!')

        print('Enter QUIT to stop, or press Enter to play another round: ')
        response = input('> ')
        if response.lower().startswith('q'):
            sys.exit()


if __name__ == '__main__':
    main()
