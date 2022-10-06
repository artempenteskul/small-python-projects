import sys
import time
import random
import shutil


MIN_STREAM_LEN = 6
MAX_STREAM_LEN = 14

PAUSE = 0.1
DENSITY = 0.04
STREAM_CHARS = ['0', '1']

WIDTH = shutil.get_terminal_size()[0] - 1


def main():
    print('The Matrix Digital Stream!')
    print('Press Ctrl-C to QUIT')
    time.sleep(2)

    try:
        columns = [0] * WIDTH
        while True:
            for i in range(WIDTH):
                if columns[i] == 0:
                    if random.random() <= DENSITY:
                        columns[i] = random.randint(MIN_STREAM_LEN, MAX_STREAM_LEN)

                if columns[i] > 0:
                    print(random.choice(STREAM_CHARS), end='')
                    columns[i] -= 1
                else:
                    print(' ', end='')

            print()
            sys.stdout.flush()
            time.sleep(PAUSE)

    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()
