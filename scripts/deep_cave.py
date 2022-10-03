import sys
import time
import random


WIDTH = 100
PAUSE_AMOUNT = .05


def main():
    print('The Deep Cave!')
    print('Press Ctrl-C to stop ...')
    print()

    left_width = 20
    gap_width = 10

    while True:
        right_width = WIDTH - left_width - gap_width
        print(('#' * left_width) + (' ' * gap_width) + ('#' * right_width))

        try:
            time.sleep(PAUSE_AMOUNT)
        except KeyboardInterrupt:
            sys.exit()

        dice_roll = random.randint(1, 6)
        if dice_roll == 1 and left_width > 1:
            left_width -= 1
        elif dice_roll == 2 and left_width + gap_width < WIDTH - 1:
            left_width += 1
        else:
            pass


if __name__ == '__main__':
    main()
