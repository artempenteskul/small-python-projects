import sys
import copy


TOTAL_DISKS = 5

COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    print('The Tower of Hanoi')
    print('Move the tower of disks, one disk at a time, to another tower.')
    print('Larger disks cannot rest on top of a smaller disk.')
    print()

    towers = {'A': copy.copy(COMPLETE_TOWER), 'B': [], 'C': []}

    while True:
        display_towers(towers)
        from_tower, to_tower = ask_for_move(towers)
        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)

        if COMPLETE_TOWER in (towers['B'], towers['C']):
            display_towers(towers)
            print()
            print(f'You have solved the puzzle! Try to increase the amount of disks ot {TOTAL_DISKS + 1}!')
            sys.exit()


if __name__ == '__main__':
    main()

