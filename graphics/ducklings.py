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
    print('The Ducklings Graphics Program!')
    print('Press Ctrl-C to QUIT.')
    time.sleep(2)

    duckling_lanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:
        for lane_num, duckling_obj in enumerate(duckling_lanes):
            if duckling_obj is None and random.random() <= DENSITY:
                duckling_obj = Duckling()
                duckling_lanes[lane_num] = duckling_obj

            if duckling_obj is not None:
                print(duckling_obj.get_next_body_part(), end='')
                if duckling_obj.part_to_display_next is None:
                    duckling_lanes[lane_num] = None
            else:
                print(' ' * DUCKLING_WIDTH, end='')

        print()
        sys.stdout.flush()
        time.sleep(PAUSE)


class Duckling:
    pass


if __name__ == '__main__':
    main()
