import sys
import time
import random


SPACE = ' '
SNAIL = '@v'
FINISH_LINE = random.randint(40, 80)
MAX_NUM_SNAILS = 8


def main():
    print(f'The Snail Race! {SNAIL}')
    print(f'{SNAIL} <-- snail')
    print()

    while True:
        print(f'How many snails will race? Max: {MAX_NUM_SNAILS}')
        response = input('> ')
        if response.isdecimal():
            num_snails = int(response)
            if 1 < num_snails <= MAX_NUM_SNAILS:
                break
        print(f'Enter a number between 2 and {MAX_NUM_SNAILS}')

    snail_names = []
    for i in range(1, num_snails + 1):
        while True:
            print(f'Enter snail #{i} name: ')
            name = input('> ').rstrip()
            if len(name) == 0:
                print('Name cannot be blank. Please enter your name.')
            elif name in snail_names:
                print('Choose a name that has not already been used.')
            elif len(name) > 20:
                print('Name cannot be longer than 20 characters, choose another.')
            else:
                break
        snail_names.append(name)

    print('\n' * 50)
    print(f'START{SPACE * (FINISH_LINE - len("START"))}FINISH')
    print(f'|{SPACE * (FINISH_LINE - len("|"))}|')

    snail_progress = {}
    for snail_name in snail_names:
        print(snail_name)
        print(SNAIL)
        snail_progress[snail_name] = 0

    time.sleep(2)

    while True:
        for i in range(random.randint(1, num_snails // 2)):
            random_snail_name = random.choice(snail_names)
            random_snail_progress = random.randint(1, 3)
            snail_progress[random_snail_name] += random_snail_progress

            if snail_progress[random_snail_name] >= FINISH_LINE:
                print()
                print(f'{random_snail_name} has won!')
                sys.exit()

        time.sleep(0.5)

        print('\n' * 50)
        print(f'START{SPACE * (FINISH_LINE - len("START"))}FINISH')
        print(f'|{SPACE * (FINISH_LINE - len("|"))}|')

        for snail_name in snail_names:
            spaces = snail_progress[snail_name]
            print(f'{SPACE * spaces}{snail_name}')
            print(f'{"." * spaces}{SNAIL}')


if __name__ == '__main__':
    main()
