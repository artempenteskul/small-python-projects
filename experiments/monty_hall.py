import sys
import random


ALL_CLOSED = ('closed', 'closed', 'closed')

FIRST_GOAT = ('goat', 'unknown', 'unknown')
SECOND_GOAT = ('unknown', 'goat', 'unknown')
THIRD_GOAT = ('unknown', 'unknown', 'goat')

FIRST_CAR = ('car', 'goat', 'goat')
SECOND_CAR = ('goat', 'car', 'goat')
THIRD_CAR = ('goat', 'goat', 'car')


def main():
    print('The Monty Hall Experiment')
    print('You can read more about Monty Hall Problem at https://en.wikipedia.org/wiki/Monty_Hall_problem')
    print()

    input('Press Enter to start ...')
    print()

    swap_wins = 0
    swap_losses = 0
    stay_wins = 0
    stay_losses = 0

    while True:
        door_with_car = random.randint(1, 3)
        show_doors(ALL_CLOSED)
        print()
        while True:
            print('Pick a door 1, 2, or 3 (or "q" to stop): ')
            response = input('> ').lower()
            if response.startswith('q'):
                print('Thanks for playing!')
                sys.exit()

            if response in ('1', '2', '3'):
                break

        print()

        door_pick = int(response)

        while True:
            door_with_goat = random.randint(1, 3)
            if door_with_goat != door_pick and door_with_goat != door_with_car:
                break

        if door_with_goat == 1:
            show_doors(FIRST_GOAT)
        elif door_with_goat == 2:
            show_doors(SECOND_GOAT)
        elif door_with_goat == 3:
            show_doors(THIRD_GOAT)

        print()
        print(f'Door {door_with_goat} contains a goat!')
        print()

        while True:
            print('Do you want to swap you choice? Y/N: ')
            swap = input('> ').lower()
            if swap in ('y', 'n'):
                break

        if swap == 'y':
            if door_pick == 1 and door_with_goat == 2:
                door_pick = 3
            elif door_pick == 1 and door_with_goat == 3:
                door_pick = 2
            elif door_pick == 2 and door_with_goat == 1:
                door_pick = 3
            elif door_pick == 2 and door_with_goat == 3:
                door_pick = 1
            elif door_pick == 3 and door_with_goat == 1:
                door_pick = 2
            elif door_pick == 3 and door_with_goat == 2:
                door_pick = 1

        if door_with_car == 1:
            show_doors(FIRST_CAR)
        elif door_with_car == 2:
            print(SECOND_CAR)
        elif door_with_goat == 3:
            print(THIRD_CAR)

        print()
        print(f'Door {door_with_car} has the car!', end=' ')

        if door_pick == door_with_car:
            print('You won!')
            if swap == 'y':
                swap_wins += 1
            elif swap == 'n':
                stay_wins += 1
        else:
            print('Sorry, but you lost!')
            if swap == 'y':
                swap_losses += 1
            elif swap == 'n':
                stay_losses += 1

        total_swaps = swap_wins + swap_losses
        if total_swaps != 0:
            swap_success = round(swap_wins / total_swaps * 100, 1)
        else:
            swap_success = 0.0

        total_stays = stay_wins + stay_losses
        if total_stays != 0:
            stay_success = round(stay_wins / total_stays * 100, 1)
        else:
            stay_success = 0.0

        print()
        print(f'Swap results: {swap_wins} wins, {swap_losses} losses, success rate - {swap_success}%')
        print(f'Stay results: {stay_wins} wins, {stay_losses} losses, success rate - {stay_success}%')
        print()

        input('Press Enter to repeat the experiment and get more accurate results ...')


def show_doors(doors):
    for door_n, door_value in enumerate(doors):
        if door_n == len(doors) - 1:
            print(f'{door_value.upper()}')
        else:
            print(f'{door_value.upper()} -- ')


if __name__ == '__main__':
    main()
