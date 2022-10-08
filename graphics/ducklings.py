import sys
import time
import shutil
import random


PAUSE = 0.2
DENSITY = 0.1

DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

WIDTH = shutil.get_terminal_size()[0] - 1


def main():
    print('The Duckling Graphics Program!')
    print('Press Ctrl-C to QUIT.')
    time.sleep(2)


if __name__ == '__main__':
    main()
