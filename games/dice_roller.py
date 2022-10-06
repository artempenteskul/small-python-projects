import sys
import random


def main():
    print('The Dice Roller!')
    print('Enter what kind and how many dices to roll.')
    print('The format is the number of dices, followed by "d", followed by the number of sides the dice have.')
    print('You can also add plus or minus adjustment.')

    while True:
        try:
            dice_str = input('> ')
            if dice_str.upper().startswith('Q'):
                print('Thanks for playing!')
                sys.exit()

            dice_str = dice_str.lower().replace(' ', '')

            d_index = dice_str.find('d')
            if d_index == -1:
                raise Exception('Missing the "d" character!')

            number_of_dices = dice_str[:d_index]
            if not number_of_dices.isdecimal():
                raise Exception('Missing the number of dices!')

            number_of_dices = int(number_of_dices)

            mod_index = dice_str.find('+')
            if mod_index == -1:
                mod_index = dice_str.find('-')

            if mod_index == -1:
                number_of_sides = dice_str[d_index+1:]
            else:
                number_of_sides = dice_str[d_index+1:mod_index]

            if not number_of_sides.isdecimal():
                raise Exception('Missing number of sides!')

            number_of_sides = int(number_of_sides)

            if mod_index == -1:
                mod_amount = 0
            else:
                mod_amount = int(dice_str[mod_index+1:])
                if dice_str[mod_index] == '-':
                    mod_amount = -mod_amount

            rolls = []
            for i in range(number_of_dices):
                roll_res = random.randint(1, number_of_sides)
                rolls.append(roll_res)

            print(f'Total: {sum(rolls) + mod_amount}.')
            print('Each dice: ', end='')

            rolls_str = [str(x) for x in rolls]
            print(', '.join(rolls_str), end=', ')

            if mod_amount != 0:
                mod_sign = dice_str[mod_index]
                print(f'{mod_sign}{abs(mod_amount)}')

        except Exception as e:
            print('Invalid input! Enter something like "3d6" or "1d10+2".')
            print(f'Input was invalid because: {str(e)}.')
            continue


if __name__ == '__main__':
    main()
